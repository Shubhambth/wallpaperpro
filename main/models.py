

from django.db import models

class Wallpaper(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='wallpapers/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MobileWallpaper(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mobile/wallpapers/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
