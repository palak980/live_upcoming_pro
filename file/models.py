from django.db import models

# Create your models here.
class profilemodel(models.Model):
    Name=models.CharField(max_length=500,null=True,blank=True)
    Email=models.CharField(max_length=500,null=True,blank=True)
    profile_photo=models.ImageField()
    companyName=models.CharField(max_length=200,null=True,blank=True)
    projectDescription = models.CharField(max_length=10000,null=True,blank=True)
    requiredSkill=models.CharField(max_length=700,null=True,blank=True)
    projectDuration=models.CharField(max_length=100,null=True,blank=True)
    bidingPrice=models.CharField(max_length=500,null=True,blank=True)
    hireText=models.CharField(max_length=500,null=True,blank=True)
    expectedPrice=models.CharField(max_length=100,null=True,blank=True)
    deliveryDate=models.DateField(null=True,blank=True)
    token=models.CharField(max_length=50,null=True,blank=True)

    
    def __str__(self):
        return self.projectName
    
   