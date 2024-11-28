from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ParkingAreaViewSet, ParkingSpotViewSet

router = DefaultRouter()
router.register(r'parking-areas', ParkingAreaViewSet, basename='parkingarea')
router.register(r'parking-spots', ParkingSpotViewSet, basename='parkingspot')

urlpatterns = [
    path('api/', include(router.urls)),
]