from django.db import models


# Create your models here.
class Friends(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    sideways = models.BooleanField(default=False)
    message = models.TextField(max_length=5000, verbose_name='', blank=True, null=True)


class Family(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    sideways = models.BooleanField(default=False)
    message = models.TextField(max_length=5000, verbose_name='', blank=True, null=True)


class Lovelies(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    sideways = models.BooleanField(default=False)
    message = models.TextField(max_length=5000, verbose_name='', blank=True, null=True)


class Video(models.Model):
    name = models.CharField(max_length=50)
    key = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    video_file = models.FileField(upload_to="myapp/static/myapp/videos/", null=True, blank=True)
    videoflag = models.BooleanField(default=False)
