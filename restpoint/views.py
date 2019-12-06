from .models import Location, Review
from .serializers import LocationSerializer, ReviewSerializer
from rest_framework import viewsets
from django.db.models import Avg

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.annotate(
            avg_reviews=Avg('reviews__rating')
        )

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
