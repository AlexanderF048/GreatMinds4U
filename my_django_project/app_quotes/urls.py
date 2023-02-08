from django.urls import path
from . import views

app_name = 'app_quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('quotes/', views.def_quotes, name='quotes'),
    path('authors/', views.def_authors, name='authors'),
    path('authors_single/', views.def_author_single, name='author_s'),

]  # по имени main будем обращаться в шаблонах
