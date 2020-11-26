from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Review, People, UserMovieScore, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    like_peoples = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    like_reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    scores = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'like_peoples', 'reviews', 'like_reviews', 'scores', 'comments')
