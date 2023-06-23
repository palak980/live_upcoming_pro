from django.db.models import fields
from rest_framework import serializers
from .models import *
  
class MysubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mysubs
        fields = ('__all__')