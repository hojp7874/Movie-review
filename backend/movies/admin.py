from django.contrib import admin
from .models import Movie, Review, People, UserMovieScore, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(People)
admin.site.register(UserMovieScore)
admin.site.register(Comment)