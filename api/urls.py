from django.urls import path
from .views import (GetMyPersonalInfo, MyPersonalInfoCallback)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="ANBK Test API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@anbk.ai"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'api'

urlpatterns = [
    path('getmyinfo/', GetMyPersonalInfo.as_view(), name='getmyinfo'),
    path('sendmyinfo/', MyPersonalInfoCallback.as_view(), name='sendmyinfo'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
