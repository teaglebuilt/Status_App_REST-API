from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerializer


class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'uri',
            'content',
            'image'
        ]

    def get_uri(self, obj):
        return "api/status/{id}".format(id=obj.id)


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'uri',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def get_uri(self, obj):
        return "api/status/{id}".format(id=obj.id)

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError(
                "Content or image cannot be blank")
        return data
