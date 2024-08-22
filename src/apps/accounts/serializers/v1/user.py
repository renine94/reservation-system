from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from src.apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password2", "is_staff", "is_active", "created_at"]
        read_only_fields = ["created_at"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise ValidationError("password 가 같은지 다시 확인 해주세요.")
        return data


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
