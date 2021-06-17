from django.test import TestCase

from .models import Movie, Review, People, UserMovieScore, Comment

# Create your tests here.
sample_movieCd = Movie.objects.all()[0].pk

class UserMovieScoreModelTests(TestCase):
    def test_under_score(self):
        under_score = UserMovieScore(score=1)
        self.assertIs(under_score.validator(), False)
# def create_score(user, movie, score):
#     return UserMovieScore.objects.create(user=user, movie=movie, score=score)

# class MovieScoreViewTest(TestCase):
#     def test_under_score(self):
#         under_score = create_score(user='admin', movie=sample_movieCd, score=0)
        