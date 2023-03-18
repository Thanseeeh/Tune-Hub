from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
