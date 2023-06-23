from django.db import models

# Create your models here.
class Mysubs(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=20000,null=True,blank=True)
    whatsapp=models.CharField(max_length=13,null=True,blank=True)