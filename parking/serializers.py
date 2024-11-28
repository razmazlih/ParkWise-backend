from rest_framework import serializers
from .models import ParkingArea, ParkingSpot
from django.db.models import Count, Q


class ParkingAreaSerializer(serializers.ModelSerializer):
    parking_spots = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    occupancy_rate = serializers.SerializerMethodField()

    class Meta:
        model = ParkingArea
        fields = [
            "id",
            "city",
            "address",
            "max_places",
            "available_places",
            "available_accessible",
            "parking_spots",
            "occupancy_rate",
        ]

    def get_occupancy_rate(self, obj):
        data = obj.parking_spots.aggregate(
            total_spots=Count("id"), occupied_spots=Count("id", filter=Q(occupied=True))
        )
        total_spots = data["total_spots"]
        occupied_spots = data["occupied_spots"]
        return (occupied_spots / total_spots) * 100 if total_spots else 0


class ParkingSpotSerializer(serializers.ModelSerializer):
    area = serializers.PrimaryKeyRelatedField(
        queryset=ParkingArea.objects.all()
    )

    class Meta:
        model = ParkingSpot
        fields = ["id", "place_position", "occupied", "accessible", "area"]
