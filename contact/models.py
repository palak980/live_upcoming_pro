from django.db import models

# Create your models here.
class Mymsg(models.Model):
    first_name=models.CharField(max_length=200,null=True,blank=True)
    last_name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=20000,null=True,blank=True)
    whatsapp=models.CharField(max_length=13,null=True,blank=True)
    msg=models.TextField(null=True,blank=True)
