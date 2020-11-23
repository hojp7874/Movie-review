from rest_framework import serializers
from .models import Movie, Review, People, UserMovieScore


class MovieSerializer(serializers.ModelSerializer):
    peoples = serializers.PrimaryKeyRelatedField(queryset=People.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["id", "movie", "title", "content"]


class PeopleSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)

    class Meta:
        model = People
        fields = ["name", "role", "photo", "movies"]

    
class UserMovieScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMovieScore
        fields = "__all__"