from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    user= models.ForeignKey(User, models.PROTECT)
    room_type = models.CharField(max_length=50)
    street=models.CharField(max_length=50, default='abc')
    room_address = models.CharField(max_length=100)
    eircode = models.CharField(max_length=20, default='D02 R590')
    number = models.IntegerField()
    image = models.ImageField(upload_to='room')
    rent = models.FloatField()
    desc = models.TextField(default='abc')