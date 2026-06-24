from .views import (UserProfileViewSet,CityViewSet,PropertyListViewSet,PropertyDetailViewSet,ImagePropertyViewSet,
                    BookingCreateViewSet,BookingApproveViewSet,ReviewViewSet,AmenityViewSet,RegisterView,CustomLoginView,LogoutView)
from rest_framework import routers
from django.urls import path,include


router = routers.DefaultRouter()


router.register(r'user_profile',UserProfileViewSet,basename='user_profile')
router.register(r'city',CityViewSet,basename='city')
router.register(r'image_property',ImagePropertyViewSet,basename='image_property')
router.register(r'review',ReviewViewSet,basename='review')
router.register(r'amenity',AmenityViewSet,basename='amenity')



urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('property/',PropertyListViewSet.as_view(),name='property_list'),
    path('property/<int:pk>/',PropertyDetailViewSet.as_view(),name='property_detail'),

    path('booking/',BookingCreateViewSet.as_view(),name='booking_create'),
    path('booking/<int:pk>',BookingApproveViewSet.as_view(),name='booking_approve'),
]
