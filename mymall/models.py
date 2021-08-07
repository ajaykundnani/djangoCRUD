from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=10)
    image = models.ImageField(null=True,blank=True,upload_to='userspic/')
