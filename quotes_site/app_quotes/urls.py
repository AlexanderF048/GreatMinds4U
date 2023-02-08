from django.urls import  path

from . import views

app_name = 'app_quotes'

urlpatterns = [
    path('', views.main_page, name='main_page'),
]



