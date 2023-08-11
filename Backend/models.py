from django.db import models

# Create your models here.
class Catdb(models.Model):
    Cna =models.CharField(max_length=70,null=True,blank=True)
    Im =models.ImageField(upload_to="profile")
    Des =models.CharField(max_length=80,null=True,blank=True)
    Price =models.CharField(max_length=50,null=True,blank=True)
    Quantity =models.CharField(max_length=70,null=True,blank=True)
    Vin =models.CharField(max_length=80,null=True,blank=True)
    Varieties =models.CharField(max_length=100,null=True,blank=True)

