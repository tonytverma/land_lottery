from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.TextField(max_length=20)
    message=models.TextField()
