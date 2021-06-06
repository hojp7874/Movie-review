from django.urls import path
from . import views


urlpatterns = [
    path('', views.DataPipelineView.as_view()),
    path('people/', views.people_list),

    # 영화 평점
    path('score', views.TestMovieScoreView.as_view()),
    path('<int:movie_pk>/score', views.MovieScoreView.as_view()),

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