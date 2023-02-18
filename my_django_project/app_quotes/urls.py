from django.urls import path
from . import views

app_name = 'app_quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('quotes/', views.def_quotes, name='quotes'),####<int:page>
    path('authors/', views.def_authors, name='authors'),
    path('authors_single/<str:author_here>', views.def_author_single, name='author_s'),
    path('quotes/<str:recived_tag>', views.def_tag_clic, name='quote_s'),
    path('add_quote/', views.def_add_quote, name='add_quote'),

]  # по имени main будем обращаться в шаблонах
#Устаревший способ - передать аргумент в функцию, зарегмстрировав тут , второй будет в тегах (модуль 10 часть 1 шаблоны)