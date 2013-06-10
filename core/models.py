from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False)

class State(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False)
    country = models.ForeignKey(Country)

class City(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False)
    state = models.ForeignKey(State)



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(
        upload_to = "photos/users/profile",
        blank = True,
        width_field = "profile_pic_width",
        height_field = "profile_pic_height"
    ),
    profile_pic_width = models.CharField(max_length = 100)
    profile_pic_height = models.CharField(max_length = 100)
    dob = models.DateField(blank = False)
    gender = models.CharField(
        max_length = '1',
        choices = (
            ('m','Male'),
            ('f','Female')
        )
    ),
    zipcode = models.IntegerField(max_length = 20)
    street_address1 = models.TextField(max_length = 500)
    street_address2 = models.TextField(max_length = 500)
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    city = models.ForeignKey(City)

class SocialNetwork(models.Model):
    name = models.CharField(max_length = 100)
    secret_token = models.CharField(max_length = 1000)
    secret_key = models.CharField(max_length = 1000)
    
class UserSocialNetwork(models.Model):
    user = models.ForeignKey(User)
    social_network = models.ForeignKey(SocialNetwork)
    auth_token = models.CharField(max_length = 1000)

    

