from django.urls import path
from . import views


urlpatterns = [
    path('movie_list_create/', views.movie_list_create),
    path('people_list/', views.people_list),
    path('<int:movie_pk>/movie_score_list_create/', views.movie_score_list_create),
    path('<int:movie_pk>/review_list_create/', views.review_list_create),
    path('<int:review_pk>/comment_list_create/', views.comment_list_create),
    path('<int:review_pk>/review_update_delete/', views.review_update_delete),
    path('<int:review_pk>/review_like/', views.review_like),
]