from django.db import models

# Create your models here.

class Cars(models.Model):

    Make = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    price = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)