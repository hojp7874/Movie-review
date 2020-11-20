from django.db import models
from django.conf import settings

class Movie(models.Model):
    # 영화 코드
    movieCd = models.CharField(max_length=50)

    # 영화 제목
    movieNm = models.CharField(max_length=50)

    # 영화 제목(영문)
    movieNmEn = models.CharField(max_length=50, blank=True)

    # 제작년도
    prdtYear = models.CharField(max_length=50)

    # 개봉일
    openDt = models.CharField(max_length=50, blank=True)

    # 장편/단편
    typeNm = models.CharField(max_length=50)

    # 개봉여부
    prdtStatNm = models.CharField(max_length=50)

    # 제작참여국가
    nationAlt = models.CharField(max_length=50)

    # 장르
    genreAlt = models.CharField(max_length=50)
    
    # 대표제작국가
    repNationNm = models.CharField(max_length=50)
    
    # 대표장르
    repGenreNm = models.CharField(max_length=50)
    
    # 감독
    directors = models.CharField(max_length=50, blank=True)
    
    # 제작사
    companys = models.CharField(max_length=50, blank=True)

    # 영화 포스터
    posterSrc = models.TextField(null=True)

    # 관객 수
    popularity = models.CharField(max_length=20, null=True)

    # 영화 예고편
    # trailer

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=50)
    content = models.TextField()