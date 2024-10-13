from django.urls import include, path
from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    path('login', views.LogIn, name="login"),
    path('signup', views.SignUp, name="signup"),
    path(
        'logout/', views.LogoutAccount, name="logout"
    ),
    path(
        'create/', views.CreateAccount, name="create-account"
    ),
    
]
