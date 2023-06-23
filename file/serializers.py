from django.db.models import fields
from rest_framework import serializers
from .models import *
  
class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profilemodel
        fields = ('__all__')