from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField
# Create your models here.

class shop_model2(models.Model):
	shop_name=models.CharField(max_length=25)
	shop_location=models.CharField(max_length=25) #For now location is a charfield, but after installing Postgis it must be (X,Y) values
	likes=models.ManyToManyField(User,name='likes') 
