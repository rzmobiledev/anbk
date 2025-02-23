from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from django.shortcuts import redirect

from core.config import MYINFO_CLIENT
from myinfo.client import MyInfoPersonalClientV4


class GetMyPersonalInfo(APIView):

    def get(self, request):
        oauth_state = MYINFO_CLIENT.get('oauth_state')
        callback_url = MYINFO_CLIENT.get('CALLBACK_URL')
        client = MyInfoPersonalClientV4()
        response = client.get_authorise_url(oauth_state, callback_url)
        return Response({'data': response}, status=status.HTTP_200_OK)


class MyPersonalInfoCallback(APIView):
    def post(self, request):
        data = request.data
        auth_code = data.get('auth_code')

        oauth_state = MYINFO_CLIENT.get('oauth_state')
        callback_url = MYINFO_CLIENT.get('CALLBACK_URL')
        person_data = MyInfoPersonalClientV4().retrieve_resource(auth_code, oauth_state, callback_url)
        return Response(person_data, status=status.HTTP_200_OK)
