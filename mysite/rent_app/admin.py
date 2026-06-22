from django.contrib import admin
from .models import UserProfile,City,Property,ImageProperty,Booking,Review,Amenity



class ImagePropertyInline(admin.TabularInline):
    model = ImageProperty
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImagePropertyInline]


admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Property,PropertyAdmin)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Amenity)