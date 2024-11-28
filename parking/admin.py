from django.contrib import admin
from .models import ParkingArea, ParkingSpot

@admin.register(ParkingArea)
class ParkingAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'max_places', 'available_places', 'available_accessible')
    search_fields = ('name', 'city', 'address')
    list_filter = ('city',)

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('place_position', 'occupied', 'accessible', 'area')
    search_fields = ('place_position', 'area__name')
    list_filter = ('occupied', 'area')