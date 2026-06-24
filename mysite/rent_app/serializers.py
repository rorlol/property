from rest_framework import serializers
from .models import UserProfile,City,Property,ImageProperty,Booking,Review,Amenity
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username','email','age','role','avatar']

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ImagePropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageProperty
        fields = ['image']

class BookingCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property','check_in','check_out']

class BookingApproveSerializers(serializers.ModelSerializer):
    guest = UserProfileSerializers()

    class Meta:
        model = Booking
        fields = ['property','guest','check_in','check_out','status','created_at']

class ReviewSerializers(serializers.ModelSerializer):
    guest = UserProfileSerializers()

    class Meta:
        model = Review
        fields = ['property','guest','rating','comment','created_at']

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
    get_avg_rating = serializers.SerializerMethodField()
    get_count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['id','title','description','price_per_night','city','property_type','rules','max_guests','bedrooms',
                  'bathrooms','amenities','images','owner','reviews','get_avg_rating','get_count_rating']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_rating(self,obj):
        return obj.get_count_rating()