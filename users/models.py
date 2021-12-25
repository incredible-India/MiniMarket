from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()