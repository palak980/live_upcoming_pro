from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewsClass
        fields='__all__'

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Twitter
        fields='__all__'