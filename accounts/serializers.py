from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
