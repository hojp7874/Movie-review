from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Movie, Review, People, UserMovieScore, Comment


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ["name", "role", "photo"]

    
class MovieSerializer(serializers.ModelSerializer):
    peoples = PeopleSerializer(many=True, read_only=True)
    # peoples = serializers.PrimaryKeyRelatedField(queryset=People.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "user", "movie", "title", "content"]


class UserMovieScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMovieScore
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "review", "content"]