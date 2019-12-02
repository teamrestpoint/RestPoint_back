from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Location(models.Model):
    location_name = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    has_changing_table = models.BooleanField(null=False)
    is_accessible = models.BooleanField(null=False)
    is_gender_neutral = models.BooleanField(null=False)
    is_family_bathroom = models.BooleanField(null=False)
    number_of_stalls = models.IntegerField(blank=True, null=True)

class Review(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(4), MinValueValidator(0)])
    review_text = models.TextField(blank=True, null=True)
    is_accurate = models.BooleanField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
