from rest_framework import viewsets,generics,status,permissions
from .models import UserProfile,City,Property,ImageProperty,Booking,Review,Amenity
from .serializers import (UserProfileSerializers,CitySerializers,PropertyListSerializers,PropertyDetailSerializers,
                          ImagePropertySerializers,BookingCreateSerializers,BookingApproveSerializers,ReviewSerializers,
                          AmenitySerializers,RegisterSerializer,LoginSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PropertyFilter
from .pagination import PropertyPagination

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .permission import CheckRole, CheckOwner, Approve


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PropertyListViewSet(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializers
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['title','description']
    ordering_fields = ['price_per_night']
    filterset_class = PropertyFilter
    pagination_class = PropertyPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,CheckRole]

class PropertyDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,CheckOwner]

class ImagePropertyViewSet(viewsets.ModelViewSet):
    queryset = ImageProperty.objects.all()
    serializer_class = ImagePropertySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingCreateViewSet(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingApproveViewSet(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingApproveSerializers
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at','status']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Approve]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]