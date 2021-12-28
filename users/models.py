from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()




class cart(models.Model):
    uid = models.ForeignKey(Users,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)
    item_price = models.BigIntegerField()