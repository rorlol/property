from rest_framework import viewsets,generics
from .models import UserProfile,City,Property,ImageProperty,Booking,Review,Amenity
from .serializers import (UserProfileSerializers,CitySerializers,PropertyListSerializers,PropertyDetailSerializers,
                          ImagePropertySerializers,BookingSerializers,ReviewSerializers,AmenitySerializers)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class PropertyListViewSet(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializers

class PropertyDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializers

class ImagePropertyViewSet(viewsets.ModelViewSet):
    queryset = ImageProperty.objects.all()
    serializer_class = ImagePropertySerializers

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializers

