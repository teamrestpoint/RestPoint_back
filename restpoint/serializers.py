from rest_framework import serializers
from .models import Location, Review

class LocationSerializer(serializers.ModelSerializer):
    # avg_reviews = serializers.DecimalField(max_digits=3, decimal_places=2)
    reviews = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='rating'
    )

    class Meta:
        model = Location
        fields = [
            'id',
            'location_name',
            'image_url',
            'lat',
            'long',
            'address',
            'description',
            'directions',
            'has_changing_table',
            'is_accessible',
            'is_gender_neutral',
            'is_family_bathroom',
            'number_of_stalls',
            # 'avg_reviews',
            'reviews',
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'location',
            'rating',
            'review_text',
            'is_accurate',
            'created_date',
        ]
