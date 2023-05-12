from django.db import models

# Create your models here.

class Service(models.Model):
    name=models.CharField(max_length=50)
    head=models.CharField(max_length=100)
    desc=models.TextField()
    image= models.ImageField(upload_to='service', default='abc')