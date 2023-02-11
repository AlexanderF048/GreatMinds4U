from django.urls import path
from . import views



app_name = 'app_users'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),# Эти функции можно не прописывать а подгрузить from
    # django.contrib.auth.views import LoginView, LogoutView
    path('logout/', views.logoutuser, name='logout'),
]