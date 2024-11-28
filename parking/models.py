from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ValidationError
import re


def validate_place_position(value):
    if not re.match(r"^[A-Z][0-9]+$", value):
        raise ValidationError(
            f"{value} is not a valid place position. It must start with a letter followed by numbers."
        )


class ParkingArea(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    max_places = models.IntegerField(editable=False, default=0)
    available_places = models.IntegerField(editable=False, default=0)
    available_accessible = models.IntegerField(editable=False, default=0)

    def update_available(self):
        self.available_places = self.parking_spots.filter(
            occupied=False, accessible=False
        ).count()
        self.available_accessible = self.parking_spots.filter(
            occupied=False, accessible=True
        ).count()
        self.max_places = self.parking_spots.count()
        self.save()

    class Meta:
        unique_together = ("city", "address")

    def __str__(self):
        return self.name


class ParkingSpot(models.Model):
    place_position = models.CharField(
        max_length=5, validators=[validate_place_position]
    )
    occupied = models.BooleanField(default=False)
    accessible = models.BooleanField(default=False)
    area = models.ForeignKey(
        ParkingArea, on_delete=models.CASCADE, related_name="parking_spots"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.area.update_available()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.area.update_available_places()

    def __str__(self):
        return f"{self.place_position} - occupied: {self.occupied}, accessible: {self.accessible}"
