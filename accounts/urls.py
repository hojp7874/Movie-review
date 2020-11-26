from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('get-users/', views.get_users),
    
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('token-verify/', refresh_jwt_token),
    path('token-refresh/', verify_jwt_token),

    path('user_update_delete/', views.user_update_delete),
    path('profile/', views.profile),
]
