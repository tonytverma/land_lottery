from django.db import models
from land.models import Room
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    booking_username=models.CharField(max_length=30, default='jagan')
    user = models.ForeignKey(User, models.PROTECT, default=1)
    room = models.ForeignKey(Room, models.PROTECT, default=1)
    fname = models.CharField(max_length=50, default='abc')
    lname = models.CharField(max_length=50, default='abc')
    email = models.CharField(max_length=50, default='abc')
    country = models.CharField(max_length= 15, default='abc')
    number = models.IntegerField( default='1234567890')
    pob = models.CharField(max_length=50, default='abc')
    noa = models.CharField(max_length=50, default='abc')
    noc = models.CharField(max_length=50, default='abc')
    sr = models.CharField(max_length=50, default='abc')
    