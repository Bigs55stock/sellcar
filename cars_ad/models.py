from django.db import models

# Create your models here.

class Cars(models.Model):

    year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    price = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


     def __str__(self):
        return self.name