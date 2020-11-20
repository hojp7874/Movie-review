from django.urls import path
from . import views


urlpatterns = [
    path('movie_list_create/', views.movie_list_create),
    path('<int:movie_pk>/review_list_create/', views.review_list_create),
    # path('', views.todo_list_create),
    # path('<int:todo_pk>/', views.todo_update_delete),
]