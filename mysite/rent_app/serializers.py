from rest_framework import serializers
from .models import UserProfile,City,Property,ImageProperty,Booking,Review,Amenity



class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username','email','role','avatar']

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ImagePropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageProperty
        fields = ['image']

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property','check_in','check_out']

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['property','rating','comment']

class AmenitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['amenity_name']

class PropertyListSerializers(serializers.ModelSerializer):
    city = CitySerializers()
    owner = UserProfileSerializers()
    amenities = AmenitySerializers(read_only=True,many=True)
    images = ImagePropertySerializers(read_only=True,many=True)

    class Meta:
        model = Property
        fields = ['id','title','description','price_per_night','city','property_type','rules','max_guests',
                  'owner','amenities','images']

class PropertyDetailSerializers(serializers.ModelSerializer):
    city = CitySerializers()
    owner = UserProfileSerializers()
    amenities = AmenitySerializers(read_only=True,many=True)
    images = ImagePropertySerializers(read_only=True,many=True)

    class Meta:
        model = Property
        fields = ['id','title','description','price_per_night','city','property_type','rules','max_guests','bedrooms',
                  'bathrooms','amenities','images','owner','reviews']