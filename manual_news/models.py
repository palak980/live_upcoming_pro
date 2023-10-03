from django.db import models

# Create your models here.
class NewsClass(models.Model):
    upload_video=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    photo=models.FileField(upload_to='docs/',null=True,blank=True)
    upload_photo=models.ImageField(upload_to='docs/photo/',null=True,blank=True)
    title=models.CharField(max_length=10000000,null=True,blank=True)
    description=models.CharField(max_length=10000000,null=True,blank=True)
    date=models.DateField(null=True,blank=True)

class Twitter(models.Model):
    chtml=models.TextField(null=True,blank=True)