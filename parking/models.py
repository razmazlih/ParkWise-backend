from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ValidationError


class ParkingArea(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    max_places = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        help_text="Enter a number between 1 and 1000",
    )
    available_places = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    def clean(self):
        if self.available_places > self.max_places:
            raise ValidationError({'available_places': 'Available places must not exceed max places.'})

    class Meta:
        unique_together = ("city", "address")

    def __str__(self):
        return self.name


class ParkingSpot(models.Model):
    place_position = models.CharField(max_length=5)
    occupied = models.BooleanField(default=False)
    area = models.ForeignKey(ParkingArea, on_delete=models.CASCADE, related_name='parking_spots')

    def __str__(self):
        return self.place_position