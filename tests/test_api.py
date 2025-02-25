import json
from unittest import mock
import pytest
from unittest.mock import patch
from django.urls import reverse
from rest_framework.test import APIClient
from core.logger import log
from api.views import (GetMyInfoURL, MyInfoPersonalClientV4, SendMyInfoPayload)
import requests
from . import data_response
from core import config


class TestAllAPIEndpoint():
    maxDiff = None
    client = APIClient()

    get_url = reverse('api:getmyinfo')
    post_url = reverse('api:sendmyinfo')
    headers: dict = {'Content-Type': 'application/json'}

    oauth_state = config.MYINFO_CLIENT.get('oauth_state')
    callback_url = config.MYINFO_CLIENT.get('CALLBACK_URL')
    auth_code = 'myinfo-com-8rUg3SNCFwQ8iQ7jyeRDgAPQy0bXzjB5ov2JfSuL'

    fake_response = {
        "application/json": {
            "data": "https://test.api.myinfo.gov.sg/com/v4/authorize?client_id=STG-202327956K-ABNK-BNPLAPPLN&scope=uinfin%20name%20sex%20race%20dob%20residentialstatus%20nationality%20birthcountry%20passtype%20passstatus%20passexpirydate%20employmentsector%20mobileno%20email%20regadd%20housingtype%20hdbtype%20cpfcontributions%20noahistory%20ownerprivate%20employment%20occupation%20cpfemployers%20marital&purpose_id=7ed6f2ce&response_type=code&code_challenge=3GrrsykxwcngCtjBWowFXWJbbeiKXp4KIxHOU_OCgBA&code_challenge_method=S256&redirect_uri=http://localhost:3001/callback",
        }
    }

    def test_get_url(self):
        response = self.client.get(self.get_url)
        assert response.status_code == 200

    def test_mock_get_url_response(self, mocker):
        with patch('api.views.MyInfoPersonalClientV4.get_authorise_url') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = self.fake_response

            get_spy = mocker.spy(MyInfoPersonalClientV4, 'get_authorise_url')
            obj = GetMyInfoURL()
            obj.get(requests)
            assert get_spy.spy_return.status_code == 200
            assert get_spy.spy_return.json() == self.fake_response

    def test_retrieve_my_info_unauthorized(self, mocker):
        response = self.client.post(self.post_url, {'auth_code': self.auth_code})
        assert response.status_code == 401

    def test_mock_retrieve_my_info(self, mocker):
        with patch('api.views.SendMyInfoPayload.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = data_response

            post_spy = mocker.spy(SendMyInfoPayload, "post")
            obj = SendMyInfoPayload()
            obj.post(requests)
            log(post_spy.spy_return.json())
            assert post_spy.spy_return.status_code == 200
            assert post_spy.spy_return.json() == data_response
