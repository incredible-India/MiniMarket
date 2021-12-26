from django.db import models


class vegitables(models.Model):
    vname = models.CharField(max_length=30)
    vprice = models.IntegerField()
    vinfo = models.TextField()
    vamm = models.CharField(max_length=30,null=True)
    vimg= models.ImageField(upload_to='static/imagesv/')


class grocrey(models.Model):
    gname = models.CharField(max_length=30)
    gprice = models.IntegerField()
    ginfo = models.TextField()
    gamm = models.CharField(max_length=30,null=True)
    gimg= models.ImageField(upload_to='static/imagesg/')
# Create your models here.
