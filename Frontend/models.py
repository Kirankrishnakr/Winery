from django.db import models

# Create your models here.
class Contactdb(models.Model):
    Nam =models.CharField(max_length=60,null=True,blank=True)
    Ema =models.EmailField(max_length=40,null=True,blank=True)
    Sub =models.CharField(max_length=60,null=True,blank=True)
    Mes =models.CharField(max_length=80,null=True,blank=True)

class Signupdb(models.Model):
    Name =models.CharField(max_length=70,null=True,blank=True)
    Email =models.EmailField(max_length=70,null=True,blank=True)
    Password =models.CharField(max_length=70,null=True,blank=True)
    Cpass =models.CharField(max_length=70,null=True,blank=True)

class Cartdb(models.Model):
    User =models.CharField(max_length=60,null=True,blank=True)
    Product =models.CharField(max_length=70,null=True,blank=True)
    Pprice =models.CharField(max_length=50,null=True,blank=True)
    Quan =models.IntegerField(null=True,blank=True)
    Tot =models.IntegerField(null=True,blank=True)

class Checkout(models.Model):
    First =models.CharField(max_length=40,null=True,blank=True)
    Last =models.CharField(max_length=40,null=True,blank=True)
    State =models.CharField(max_length=50,null=True,blank=True)
    Street =models.CharField(max_length=60,null=True,blank=True)
    Postal =models.IntegerField(null=True,blank=True)
    Town =models.CharField(max_length=60,null=True,blank=True)
    Phone =models.IntegerField(null=True,blank=True)
    Grat =models.CharField(max_length=60,null=True,blank=True)
