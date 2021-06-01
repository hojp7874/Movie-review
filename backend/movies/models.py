from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    # 영화 코드
    movieCd = models.CharField(primary_key=True, max_length=20)

    # 영화 제목
    movieNm = models.CharField(max_length=50)

    # 영화 제목(영문)
    movieNmEn = models.CharField(max_length=100, blank=True)

    # 제작년도
    prdtYear = models.CharField(max_length=10, blank=True)

    # 개봉일
    openDt = models.CharField(max_length=10, blank=True)

    # 장편/단편
    typeNm = models.CharField(max_length=10, blank=True)

    # 개봉여부
    prdtStatNm = models.CharField(max_length=10, blank=True)

    # 제작참여국가
    nationAlt = models.CharField(max_length=30, blank=True)

    # 장르
    genreAlt = models.CharField(max_length=30, blank=True)
    
    # 대표제작국가
    repNationNm = models.CharField(max_length=10, blank=True)
    
    # 대표장르
    repGenreNm = models.CharField(max_length=10, blank=True)
    
    # 감독
    # directors = models.CharField(max_length=50, blank=True)
    
    # 제작사
    # companys = models.CharField(max_length=10, blank=True)

    # 영화 포스터
    posterSrc = models.TextField(null=True)

    # 관객 수
    popularity = models.CharField(max_length=20, null=True)

    # 영화 예고편
    # trailer

    # 영화 줄거리
    story = models.TextField(null=True)

    # 영화 평점


# 영화 리뷰
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=50)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


# 영화 감독, 등장인물
class People(models.Model):
    movies = models.ManyToManyField(Movie, related_name='peoples')
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    photo = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_peoples')


# 영화 평점
class UserMovieScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scores')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


# 댓글
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')