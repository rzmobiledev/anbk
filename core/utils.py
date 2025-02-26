from django.utils.crypto import get_random_string


class OauthStateCallback:

    def __init__(self, oauth_state: str, callback_url: str):
        self.oauth_state = oauth_state
        self.callback_url = callback_url


def generate_random_string():
    return get_random_string(length=16)
