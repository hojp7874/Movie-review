import requests

# 영진위 api
from .movie_api import URLMaker_kobis, URLMaker_naver

# 크롤링
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer, ReviewSerializer, PeopleSerializer, UserMovieScoreSerializer, CommentSerializer
from .models import Movie, Review, People, UserMovieScore, Comment


@api_view(['GET', 'POST'])
def movie_list_create(request):
    # 영화 data 불러오기
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        # 영화 data 만들기
        for curPage in range(1, 50):
            # 영화인 목록 url 저장
            um = URLMaker_kobis()
            url = um.get_url('movie', 'searchMovieList')

            # API에 요청
            r = requests.get(f'{url}&curPage={curPage}')

            # API에 응답, movies에 data저장
            movies_dict = r.json()
            for idx in range(10):
                movie = movies_dict.get('movieListResult').get('movieList')[idx]
                if movie['companys']:
                    movie['companys'] = movies_dict.get('movieListResult').get('movieList')[idx].get('companys')[0]['companyNm']
                else:
                    movie['companys'] = ''

                movieNm = quote(movie['movieNm'])
                response = urlopen(f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={movieNm}+{quote("영화")}')
                soup = BeautifulSoup(response, 'html.parser')

                # 포스터 추가
                try:
                    movie['posterSrc'] = str(soup.select("a.thumb._item")[0].find('img')['src'])
                except:
                    continue

                # 관객 수 추가
                try:
                    for people in soup.select("dl div.info_group dd"):
                        if people.get_text()[-1] == '명':
                            movie['popularity'] = people.get_text()
                            break
                except:
                    pass

                # 줄거리 추가
                try: movie['story'] = soup.select("div.text_expand._ellipsis span")[0].get_text()
                except: pass

                # movie data 저장
                serializer = MovieSerializer(data=movie)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

                # 감독, 배우 가져오기
                movieObj = get_object_or_404(Movie, pk=movie['movieCd'])
                try:
                    peoples = soup.select("div.cm_info_box.scroll_img_vertical_87_98 div.area_card")
                    for people in peoples:
                        name = people.find("strong").get_text()
                        # 만약 이미 있는 배우라면
                        if not People.objects.filter(name=name).exists():
                            try:
                                role = people.find("span").get_text()
                                if role not in ['감독', '각본']:
                                    role = '배우'
                            except: role = '배우'
                            photo = people.find("img")["src"]
                            if photo[:4] == 'data': photo = '이미지 없음'
                            serializer = PeopleSerializer(data={"name": name, "role": role, "photo": photo})
                            print('시리얼라이저 직전')
                            if serializer.is_valid(raise_exception=True):
                                print('시리얼라이저 벨리드')
                                serializer.save()

                        # 영화와 인물 ManytoMany 매칭
                        people = get_object_or_404(People, name=name)
                        print('people 불러오기 완료')
                        people.movies.add(movieObj)
                        print('성공')

                except:
                    print('실패')
                    print(movieObj)


        movies = Movie.objects.all()[::-1]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      
# 영화 평점 불러오기, 만들기
# 만들기
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_score_create(request):
    serializer = UserMovieScoreSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


# 불러오기
@api_view(['GET'])
def movie_score_list(request, movie_pk):
    if request.method == 'GET':
        scores = UserMovieScore.objects.filter(movie=movie_pk)
        serializer = UserMovieScoreSerializer(scores, many=True)
        return Response(serializer.data)


# 영화평점 싹다 가져오기
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_score(request):
    if request.method == 'GET':
        scores = UserMovieScore.objects.filter(user=request.user)
        serializer = UserMovieScoreSerializer(scores, many=True)
        return Response(serializer.data)


# 영화평점 UD
@api_view(['PATCH', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_score_update_delete(request, movie_pk):
    score = get_object_or_404(UserMovieScore, movie=movie_pk)

    if request.method == 'PUT':
        serializer = UserMovieScoreSerializer(score, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        print('###')
        score.delete()
        return Response({ '영화 평점이 삭제되었습니다' })


# 영화인 불러오기, 만들기
@api_view(['GET'])
def people_list(request):
    # 불러오기
    peoples = People.objects.all()
    serializer = PeopleSerializer(peoples, many=True)
    return Response(serializer.data)


# 영화인, 영화 테이블 보내기
# def people_movies(request):



# 리뷰 C
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 R
@api_view(['GET'])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


# 리뷰 UD
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'})

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({ 'id': review_pk })


# 리뷰 좋아요
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        return Response({'리뷰 좋아요가 취소되었습니다.'})
    else:
        review.like_users.add(request.user)
        return Response({'리뷰 좋아요가 완료되었습니다.'})


# 코멘트 C
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 코멘트 R
@api_view(['GET'])
def comment_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = Comment.objects.filter(review=review)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 코멘트 UD
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'})

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'delete id': comment_pk })