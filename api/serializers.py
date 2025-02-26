from rest_framework import serializers
from core.utils import OauthStateCallback


class OauthStateCallbackSerializer(serializers.Serializer):
    oauth_state = serializers.CharField()
    callback_url = serializers.CharField()

    def create(self, validated_data):
        return OauthStateCallback(**validated_data)

    def update(self, instance, validated_data):
        instance.oauth_state = validated_data.get('state', instance.oauth_state)
        instance.callback_url = validated_data.get('callback', instance.callback_url)
        return instance
