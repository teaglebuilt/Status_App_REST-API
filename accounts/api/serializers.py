from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.reverse import reverse as api_reverse
from django.utils import timezone
import datetime


User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]

    def get_uri(self, obj):
        request = self.context.get("request")
        return api_reverse("api-user:detail", kwargs={'username': obj.username}, request=request)


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
            'expires',
            'message'
        ]

        def get_message(self, obj):
            return "Thank you for registering. Please verify your email before continuing."

        def validate_username(self, value):
            qs = User.objects.filter(username__iexact=value)
            if qs.exists():
                raise serializers.ValidationError(
                    "A User with this username already exists")
            return value

        def validate_email(self, value):
            qs = User.objects.filter(email__iexact=value)
            if qs.exists():
                raise serializers.ValidationError(
                    "A User with this email already exists")
            return value

        def get_token(self, obj):
            user = obj
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return token

        def get_expires(self, obj):
            return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

        def create(self, validated_data):
            # print(validated_data)
            user_obj = User(
                username=validated_data.get('username'),
                email=validated_data.get('email'))
            user_obj.set_password(validated_data.get('password'))
            user_obj.is_active = False
            user_obj.save()
            return user_obj
