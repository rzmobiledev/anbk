import base64
import logging
from hashlib import sha256
from json import JSONDecodeError
from urllib.parse import quote, urlencode

import requests
from myinfo import settings
from myinfo.security import (
    decrypt_jwe,
    generate_client_assertion,
    generate_code_challenge,
    generate_dpop_header,
    generate_ephemeral_session_keypair,
    get_jwkset,
    verify_jws,
)
from requests import HTTPError

log = logging.getLogger(__name__)


class MyInfoClient(object):
    """
    See API doc at https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v3.1.1.html
    Test data: https://www.ndi-api.gov.sg/library/trusted-data/myinfo/resources-personas.
    """

    API_TIMEOUT = 30
    # MyInfo fields
    context = ""
    version = ""
    client_id = ""

    def __init__(self, name=None):
        """
        Initialize a request session to interface with remote API
        """
        self.session = requests.Session()

    @classmethod
    def get_url(cls, resource: str):
        """
        Returns the URL for resource.
        Refer to URL structure at
        https://public.cloud.myinfo.gov.sg/myinfobiz/myinfo-biz-specs-v2.0.1.html#section/Environments
        """

        #  https://public.cloud.myinfo.gov.sg/myinfobiz/myinfo-biz-specs-v2.0.1.html#section/Environments
        return f"{settings.MYINFO_DOMAIN}/{cls.context}/{cls.version}/{resource}"

    def request(self, api_url, method="GET", extra_headers=None, params=None, data=None):
        """
        Returns:
            dict or str

        Raises:
            requests.RequestException
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        if extra_headers:
            headers.update(extra_headers)

        # log.debug("headers = %s", headers)
        response = self.session.request(
            method,
            url=api_url,
            params=params,
            data=data,
            timeout=self.API_TIMEOUT,
            verify=settings.CERT_VERIFY,
            headers=headers,
        )

        try:
            response.raise_for_status()
        except HTTPError as e:
            log.exception("HTTPError: %s", e.response.content)
            raise

        try:
            return response.json()
        except JSONDecodeError:
            return response.text


class MyInfoPersonalClientV4(MyInfoClient):
    """
    See https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.html
    """
    context = "com"
    version = "v4"
    client_id = settings.MYINFO_CLIENT_ID
    purpose_id = settings.MYINFO_PURPOSE_ID  # Identity verification and credit assessment

    def get_retrieve_resource_url(self, sub: str) -> str:
        return self.get_url("person") + f"/{sub}/"

    @classmethod
    def get_authorise_url(cls, oauth_state: str, callback_url: str) -> str:
        """
        Return a redirect URL to SingPass login page for user's authentication and consent.
        """
        code_challenge = generate_code_challenge(oauth_state)

        query = {
            "client_id": cls.client_id,
            "scope": cls.get_scope(),
            "purpose_id": cls.purpose_id,
            "response_type": "code",
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
            "redirect_uri": callback_url,
        }
        querystring = urlencode(query, safe=",/:", quote_via=quote)
        url = cls.get_url("authorize")
        authorise_url = f"{url}?{querystring}"
        return authorise_url

    @classmethod
    def get_scope(cls):
        return settings.MYINFO_SCOPE

    def get_access_token(
        self, auth_code: str, state: str, callback_url: str, session_ephemeral_keypair=None
    ):
        """
        Generate an access token when presented with a valid authcode obtained from the Authorise API.
        This token can then be used to request for the user's data that were consented.
        """
        api_url = self.get_url("token")
        jkt_thumbprint = session_ephemeral_keypair.thumbprint()
        client_assertion = generate_client_assertion(api_url, jkt_thumbprint)
        data = {
            "code": auth_code,
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "redirect_uri": callback_url,
            "client_assertion": client_assertion,
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "code_verifier": state,
        }
        dpop_header = generate_dpop_header(api_url, session_ephemeral_keypair)

        resp = self.request(
            api_url,
            method="POST",
            extra_headers={"DPoP": dpop_header, "Cache-Control": "no-cache"},
            data=data,
        )

        return resp

    def get_person_data(self, access_token: str, session_ephemeral_keypair):
        jwkset = get_jwkset(settings.MYINFO_JWKS_TOKEN_VERIFICATION_URL)
        decoded_access_token = verify_jws(access_token, jwkset)
        api_url = self.get_retrieve_resource_url(decoded_access_token["sub"])
        params = {
            "scope": self.get_scope(),
        }

        # generate ath to append into DPoP
        access_token_hash = sha256(access_token.encode()).digest()
        ath = base64.urlsafe_b64encode(access_token_hash).decode().replace("=", "")

        dpop_header = generate_dpop_header(
            api_url, session_ephemeral_keypair, method="GET", ath=ath
        )

        resp = self.request(
            api_url,
            method="GET",
            extra_headers={
                "Authorization": f"DPoP {access_token}",
                "dpop": dpop_header,
                "Cache-Control": "no-cache",
            },
            params=params,
        )
        return resp

    def retrieve_resource(self, auth_code: str, state: str, callback_url: str) -> dict:
        session_ephemeral_keypair = generate_ephemeral_session_keypair()
        access_token_resp = self.get_access_token(
            auth_code=auth_code,
            state=state,
            callback_url=callback_url,
            session_ephemeral_keypair=session_ephemeral_keypair,
        )
        access_token = access_token_resp["access_token"]
        person_data = self.get_person_data(access_token, session_ephemeral_keypair)

        return decrypt_jwe(person_data)
