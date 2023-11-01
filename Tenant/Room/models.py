from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


def upload_to(instance, filename):
    return '/'.join(['images', str(instance.title), filename])


def upload_to_profile_pic(instance, filename):
    return '/'.join(['profile_pics', str(instance.username), filename])



class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to=upload_to_profile_pic, default="default_profile_pic.png", null=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Apartment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="apartments")
    owner_pkey = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    bhk = models.CharField(max_length=10, default="1 BHK", null=True)
    sqft = models.IntegerField(blank=True, null=True)
    tenants = models.PositiveSmallIntegerField(blank=True, null=True)
    room_option = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    deposit = models.IntegerField(blank=True, null=True)
    room_type = models.CharField(max_length=100, choices=(('Flat', 'Flat'), ('House', 'House'), 
                                                          ('Apartment', 'Apartment'), ('Villa', 'Villa')), blank=True, null=True)


    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    photo_1 = models.ImageField(upload_to=upload_to, default='default_image.jpg', null=True)
    photo_2 = models.ImageField(upload_to=upload_to, default='default_image.jpg', null=True)
    photo_3 = models.ImageField(upload_to=upload_to, default='default_image.jpg', null=True)
    photo_4 = models.ImageField(upload_to=upload_to, default='default_image.jpg', null=True)
    list_date = models.DateTimeField(default=timezone.now, blank=True)
    
    def __str__(self):
        return str(self.title)



