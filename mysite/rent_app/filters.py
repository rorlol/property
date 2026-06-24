from django_filters.rest_framework import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'city':['exact'],
            'property_type':['exact'],
            'max_guests':['gt','lt'],
            'price_per_night':['gt','lt'],
            'amenities':['exact']
        }