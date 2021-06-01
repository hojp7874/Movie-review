from django.urls import path
from . import views


urlpatterns = [
    path('movie_list_create/', views.movie_list_create),
    path('people_list/', views.people_list),
    # 영화 평점
    path('movie_score_create/', views.movie_score_create),
    path('<int:movie_pk>/movie_score_list/', views.movie_score_list),
    path('<int:movie_pk>/movie_score_update_delete/', views.movie_score_update_delete),
    
    # 영화평점 싹다 불러오기
    path('movie_score/', views.movie_score),

    # 리뷰 CRUD, 좋아요
    path('review_create/', views.review_create),
    path('<int:movie_pk>/review_list/', views.review_list),
    path('<int:review_pk>/review_update_delete/', views.review_update_delete),
    path('<int:review_pk>/review_like/', views.review_like),
    
    # 댓글
    path('comment_create/', views.comment_create),
    path('<int:review_pk>/comment_list/', views.comment_list),
    path('<int:comment_pk>/comment_update_delete/', views.comment_update_delete),
]