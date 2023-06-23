from rest_framework import serializers
from .models import *

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model=SocialClass
        fields='__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActionClass
        fields='__all__'