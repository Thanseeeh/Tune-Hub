from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)


class Musics(models.Model):
    music_name = models.CharField(max_length=255)
    music_desc = models.CharField(max_length=255)
    music_img = models.ImageField(upload_to='musics')



