from django.urls import path
from . import views


urlpatterns = [
    path('data-pipeline/<int:total_page>', views.movie_create),
    path('all', views.movie_list),
    path('people', views.people_list),

    # 영화 평점
    path('score', views.movie_score_create_listall),
    path('<int:movie_pk>/score', views.movie_score_update_delete),
    path('<int:movie_pk>/score-read', views.movie_score_list),

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