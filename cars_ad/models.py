from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
 
class Cars(models.Model):
    make = models.CharField(max_length=150, default="")
    year = models.CharField(max_length=150,default="")
    model = models.CharField(max_length=150,default="")
    price = models.CharField(max_length=300, default="")
    mileage = models.CharField(max_length=300, default="")
    img = models.CharField(max_length=500, default="")
    desc = models.TextField(max_length=500,default="")
    contact = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
         return self.make


    