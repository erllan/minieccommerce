from django.urls import path
from .views import (userlist,
					signup, 
					update)
from .tokens import CustomAuthToken
from rest_framework.authtoken import views


urlpatterns = [
    path('users/', userlist, name='users'),
    path('signup/', signup, name='signup'),
    path('token-auth/', CustomAuthToken.as_view()),
    path('update/<str:pk>/', update, name='profile_update'),
    
]