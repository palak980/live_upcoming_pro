from django.db import models

# Create your models here.

class SocialClass(models.Model):
    upload_video=models.FileField(upload_to='docs/',null=True,blank=True)
    upload_photo=models.ImageField(upload_to='docs/photo/',null=True,blank=True)
    upload_story=models.CharField(max_length=10000000,null=True,blank=True)

class ActionClass(models.Model):
    comment=models.CharField(max_length=200)
    like=models.IntegerField()

