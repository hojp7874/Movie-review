from rest_framework import serializers
from .models import Movie, Review, People


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["id", "movie", "title", "content"]


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ["name", "role", "photo"]