from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import ParkingArea, ParkingSpot
from .serializers import ParkingAreaSerializer, ParkingSpotSerializer

class ParkingAreaViewSet(ModelViewSet):
    queryset = ParkingArea.objects.all()
    serializer_class = ParkingAreaSerializer

class ParkingSpotViewSet(ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

    @action(detail=False, methods=['get'], url_path='by-area/(?P<area_id>\d+)')
    def spots_by_area(self, request, area_id=None):
        spots = self.queryset.filter(parking_area_id=area_id)
        serializer = self.serializer_class(spots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)