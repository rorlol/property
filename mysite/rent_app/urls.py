from .views import (UserProfileViewSet,CityViewSet,PropertyListViewSet,PropertyDetailViewSet,ImagePropertyViewSet,
                    BookingViewSet,ReviewViewSet,AmenityViewSet)
from rest_framework import routers
from django.urls import path,include


router = routers.DefaultRouter()


router.register(r'user_profile',UserProfileViewSet,basename='user_profile')
router.register(r'city',CityViewSet,basename='city')
router.register(r'image_property',ImagePropertyViewSet,basename='image_property')
router.register(r'booking',BookingViewSet,basename='booking')
router.register(r'review',ReviewViewSet,basename='review')
router.register(r'amenity',AmenityViewSet,basename='amenity')



urlpatterns = [
    path('', include(router.urls)),

    path('property/',PropertyListViewSet.as_view(),name='property_list'),
    path('property/<int:pk>/',PropertyDetailViewSet.as_view(),name='property_detail'),
]
