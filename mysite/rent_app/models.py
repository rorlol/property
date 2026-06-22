from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


USER_ROLE = (
    ('host','host'),
    ('guest','guest')
)

class UserProfile(AbstractUser):
    role = models.CharField(max_length=5,choices=USER_ROLE,default='guest')
    phone_number =PhoneNumberField(region='KG',default='+996')
    avatar = models.ImageField(upload_to='avatar_image/', null=True, blank=True)

class City(models.Model):
    city_name = models.CharField(max_length=32)

class Property(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    price_per_night = models.PositiveSmallIntegerField(default=0)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    address = models.TextField()
    PROPERTY_TYPE = (
        ('apartment','apartment'),
        ('house','house'),
        ('studio','studio')
    )
    property_type = models.CharField(max_length=9,choices=PROPERTY_TYPE)
    RULES = (
        ('no_smoking','no_smoking'),
        ('pets_allowed','pets_allowed')
    )
    rules = models.CharField(max_length=12,choices=RULES)
    max_guests = models.PositiveSmallIntegerField(default=0)
    bedrooms = models.PositiveSmallIntegerField(default=0)
    bathrooms = models.PositiveSmallIntegerField(default=0)
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    property_images = models.ForeignKey

class ImageProperty(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='images_property/')

class Booking(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    guest = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    STATUS = (
        ('pending','pending'),
        ('approved','approved'),
        ('rejected','rejected'),
        ('cancelled','cancelled')
    )
    status = models.CharField(max_length=10, choices=STATUS,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='reviews')
    guest = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Amenity(models.Model):
    amenity_name = models.CharField(max_length=32,unique=True)
    amenity_icon = models.ImageField(upload_to='amenity_icon/')
    property = models.ManyToManyField(Property,related_name='amenities')