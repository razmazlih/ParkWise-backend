from rest_framework.viewsets import ModelViewSet
from .models import ParkingArea, ParkingSpot
from .serializers import ParkingAreaSerializer, ParkingSpotSerializer

class ParkingAreaViewSet(ModelViewSet):
    queryset = ParkingArea.objects.all()
    serializer_class = ParkingAreaSerializer

class ParkingSpotViewSet(ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer