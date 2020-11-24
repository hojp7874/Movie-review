from django.urls import path
from . import views


urlpatterns = [
    path('movie_list_create/', views.movie_list_create),
    path('people_list/', views.people_list),
    path('<int:movie_pk>/movie_score_list_create/', views.movie_score_list_create),

    path('review_create/', views.review_create),
    path('<int:movie_pk>/review_list/', views.review_list),
    path('<int:review_pk>/review_like/', views.review_like),
    path('<int:review_pk>/review_update_delete/', views.review_update_delete),
    
    path('comment_create/', views.comment_create),
    path('<int:review_pk>/comment_list/', views.comment_list),
    path('<int:comment_pk>/comment_update_delete/', views.comment_update_delete),
]