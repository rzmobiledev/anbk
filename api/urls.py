
from django.urls import path
from .views import (GetMyPersonalInfo, MyPersonalInfoCallback)

app_name = 'api'

urlpatterns = [
    path('', GetMyPersonalInfo.as_view(), name='api'),
    path('sendmyinfo/', MyPersonalInfoCallback.as_view(), name='sendmyinfo')
]
