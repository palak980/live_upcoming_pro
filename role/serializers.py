from rest_framework import serializers
from .models import *


class UserRegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password', 'is_admin', 'is_staff', 'is_user']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        elif data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data):
        user = CustomUser(email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_admin=validated_data['is_admin'],
            is_staff=validated_data['is_staff'],
            is_user=validated_data['is_user']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ['email', 'password']