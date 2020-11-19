import requests
from .kobis import URLMaker

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer
from .models import Movie


@api_view(['GET', 'POST'])
def movie_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()[::-1]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        for curPage in range(1, 2):
            # 영화인 목록 url 저장
            um = URLMaker()
            url = um.get_url('movie', 'searchMovieList')

            # API에 요청
            r = requests.get(f'{url}&curPage={curPage}')

            # API에 응답, movies에 data저장
            movies_dict = r.json()
            for idx in range(10):
                movie = movies_dict.get('movieListResult').get('movieList')[idx]
                try:
                    movie['directors'] = [ movies_dict.get('movieListResult').get('movieList')[idx].get('directors')[0].get('peopleNm') ]
                    print(movies_dict.get('movieListResult').get('movieList')[idx].get('directors')[0].get('peopleNm'))
                except:
                    pass
                serializer = MovieSerializer(data=movie)
                # movie_directors = (movie['directors'])
                # for movie_director in movie_directors:
                #     serializer.directorNm = movie_director['peopleNm']
                #     print(movie_director['peopleNm'])
                #     print(serializer.directorNm)
                if serializer.is_valid(raise_exception=True):
                        # serializer.companyNm = movie['companys'][0]['companyNm']
                    serializer.save()
        movies = Movie.objects.all()[::-1]
        serializer = MovieSerializer(movies, many=True)
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
