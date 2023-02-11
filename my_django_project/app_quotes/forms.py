from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.forms import ModelForm, CharField, TextInput

from .models import Quotes, Authors


class FormQuote(ModelForm):
    tags = CharField(min_length=1, max_length=50, required=True, widget=TextInput())#Тут заходит строка, далее в функции превратим ее в array
    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    quote = CharField(min_length=5, max_length=5000, required=True, widget=TextInput())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        model = Quotes
        fields = ['tags', 'author', 'quote', 'user']
        exclude = ['tags', 'author'] #так как это связь многие-ко-многим и мы ее будем обрабатывать особым способом.
