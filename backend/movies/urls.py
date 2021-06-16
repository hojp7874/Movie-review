from django.urls import path
from . import views


urlpatterns = [
    path('data-pipeline/', views.DataPipelineView.as_view()),
    path('people/', views.people_list),

    # 영화 평점
    path('score/', views.TestMovieScoreView.as_view()),
    path('<int:movie_pk>/score/', views.MovieScoreView.as_view()),

    # 리뷰 CRUD, 좋아요
    path('review/', views.review_create),
    path('<int:movie_pk>/reviews/', views.review_list),
    path('review/<int:review_pk>/', views.review_update_delete),
    path('review/<int:review_pk>/like/', views.review_like),
    
    # 댓글
    path('comment/', views.comment_create),
    path('review/<int:review_pk>/comments/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_update_delete),
]