from django.db import models


# Create your models here.
class Friends(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    message = models.CharField(max_length=5000)


class Family(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    message = models.CharField(max_length=5000)


class Lovelies(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    message = models.CharField(max_length=5000)


class Video(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myapp/static/myapp/images/", blank=True, null=True)
    video_file = models.FileField(upload_to="myapp/static/myapp/videos/", null=True, blank=True)
