import os

CERT_VERIFY = False

MYINFO_DOMAIN = "https://test.api.myinfo.gov.sg"
MYINFO_CLIENT_ID = "STG-202327956K-ABNK-BNPLAPPLN"

# https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.html#section/Authentication/OAuth2
MYINFO_SCOPE = (
    # Personal
    "uinfin name sex race dob residentialstatus nationality birthcountry "
    "passtype passstatus passexpirydate "
    "employmentsector mobileno email regadd housingtype hdbtype "
    # --- Finance
    "cpfcontributions "
    "noahistory "  # Notice of Assessment (Detailed, Last 2 Years)
    "ownerprivate "  # Ownership of Private Residential Property
    # --- Education & employment
    "employment "  # Name of Employer
    "occupation "
    "cpfemployers "  # Employers as stated in CPF Contribution History (up to 15 months)
    # --- Family
    "marital"
)

# =============== MYINFO API v4 ===============
MYINFO_JWKS_TOKEN_VERIFICATION_URL = "https://test.authorise.singpass.gov.sg/.well-known/keys.json"
MYINFO_JWKS_DATA_VERIFICATION_URL = "https://test.myinfo.singpass.gov.sg/.well-known/keys.json"
MYINFO_PURPOSE_ID = os.environ.get("MYINFO_PURPOSE_ID", "7ed6f2ce")
# ansible vault somehow replaces double quotes with single quotes.
# so we need to revert to double quotes.
MYINFO_PRIVATE_KEY_SIG = os.environ.get(
    "MYINFO_PRIVATE_KEY_SIG",
    '{"alg":"ES256","crv":"P-256","d":"Y7y4AtZ_j_4FNS0tRNYKySgdx-QcBQtjQzf1NRTHDCI","kty":"EC","use":"sig","x":"k-K2AGmjySAjxPhHLA_vCv8aa-oIoACSWhyZEQmRewc","y":"WMro28Kf4Y5Y5fiwOL-WRAo9AYFBhv8GNbtr-xnz4a0"}',  # noqa: E501
).replace("'", '"')

MYINFO_PRIVATE_KEY_ENC = os.environ.get(
    "MYINFO_PRIVATE_KEY_ENC",
    '{"alg":"ECDH-ES+A256KW","crv":"P-256","d":"fqyHyvArMu7NTc_G354VCHYqDUv0WgL8TNGg5IBpaUU","kty":"EC","use":"enc","x":"AsflFcp_M8WQxWbxImCAtJ0zWf4yHYz_3jU4faD5ODg","y":"Nc8-inmbKEOyS6VGKoZDPc2mFhugrx27lcVis9E_jWs"}',  # noqa: E501
).replace("'", '"')

# ============== /MYINFO API v4 ===============
