import unittest

from myinfo.client import MyInfoPersonalClientV4


class TestMyInfoPersonalClientV4(unittest.TestCase):
    maxDiff = None

    def test_get_authorise_url(self):
        authorise_url = MyInfoPersonalClientV4().get_authorise_url(
            "abc123", "https://backend.local.abnk.ai/myinfo/callback"
        )
        self.assertEqual(
            authorise_url,
            "https://test.api.myinfo.gov.sg/com/v4/authorize?client_id=STG-202327956K-ABNK-BNPLAPPLN&scope=uinfin%20name%20sex%20race%20dob%20residentialstatus%20nationality%20birthcountry%20passtype%20passstatus%20passexpirydate%20employmentsector%20mobileno%20email%20regadd%20housingtype%20hdbtype%20cpfcontributions%20noahistory%20ownerprivate%20employment%20occupation%20cpfemployers%20marital&purpose_id=7ed6f2ce&response_type=code&code_challenge=bKE9UspwyIPg8LsQHkJaiehiTeUdstI5JZOvaoQRgJA&code_challenge_method=S256&redirect_uri=https://backend.local.abnk.ai/myinfo/callback",  # noqa: E501
        )
