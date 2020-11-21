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

from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review




@api_view(['GET', 'POST'])
def movie_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()[::-1]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        for curPage in range(1, 2):
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
                    pass

                # 관객 수 추가
                try:
                    for people in soup.select("dl div.info_group dd"):
                        if people.get_text()[-1] == '명':
                            movie['popularity'] = people.get_text()
                            break
                except:
                    pass

                # 감독, 배우 가져오기
                try:
                    peoples = soup.select(".title_box span a")
                    for i in range(len(peoples)):
                        role = soup.select(".title_box span a")[i].get_text()
                        name = soup.select(".area_card div.thumb")[i].find("img")["alt"]
                        image = soup.select(".area_card div.thumb")[i].find("img")["src"]
                        print(role, name, image)
                        if role == '감독':
                            movie['directors'] = name
                except:
                    pass

                
                if type(movie['directors']) != str and movie['directors']:
                    movie['directors'] = movies_dict.get('movieListResult').get('movieList')[idx].get('directors')[0]['peopleNm']
                elif not movie['directors']:
                    movie['directors'] = ''

                serializer = MovieSerializer(data=movie)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
        movies = Movie.objects.all()[::-1]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.user)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['PUT', 'DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def todo_update_delete(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk)

#     if not request.user.todos.filter(pk=todo_pk).exists():
#         return Response({'detail': '권한이 없습니다.'})
        

#     if request.method == 'PUT':
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#     else:
#         todo.delete()
#         return Response({ 'id': todo_pk })
