from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cars(models.Model):
    make = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    desc = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    price = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
         return self.make


    