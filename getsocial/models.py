from django.db import models
from spiffcity import settings
from time import gmtime, strftime
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False)

class State(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False)
    country = models.ForeignKey(Country)

class City(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False)
    state = models.ForeignKey(State)


class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True, blank = False)

class Album(models.Model):
    title = models.CharField(max_length = 50, unique = True, blank = False)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

class Photo(models.Model):
    title = models.CharField(max_length = 50, unique = True, blank = False)
    album = models.ForeignKey(Album)
    image_width = models.CharField(max_length = 100)
    image_height = models.CharField(max_length = 100)
    image = models.ImageField(
        upload_to = strftime("photos/%y/%m", gmtime()),
        blank = False,
        width_field = "image_width",
        height_field = "image_height"
    )
    city = models.ForeignKey(City)
    cover_image = models.BooleanField(default = False)
    featured = models.BooleanField(default = False)
    likes_count = models.IntegerField(max_length = 100)
    comments_count = models.IntegerField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    