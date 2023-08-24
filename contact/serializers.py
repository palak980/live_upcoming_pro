from django.db.models import fields
from rest_framework import serializers
from .models import *
  
class MymsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mymsg
        fields = ('__all__')