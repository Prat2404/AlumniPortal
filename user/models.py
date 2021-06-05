from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from datetime import datetime

# Create your models here.
class Alumni(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    branch=models.CharField(max_length=50)
    year=models.IntegerField()
    degree=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    job=models.CharField(max_length=500)

class Blog(models.Model):
    author=models.ManyToManyField(User)
    blogtype=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    date=models.DateField()
    description=models.TextField()
    

