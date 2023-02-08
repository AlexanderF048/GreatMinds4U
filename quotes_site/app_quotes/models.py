from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Authors(models.Model):

    fullname = models.CharField(max_length=50, primary_key=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=250)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return f'Author: {fullname}, B_date: {born_date}, B_location: {born_location}, Descr.: {description}'


class Quotes(models.Model):
    tagss = ArrayField(ArrayField(models.CharField(max_length=20, blank=True), size=15), size=15)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, to_field='fullname')
    quote = models.CharField(max_length=5000)

    def __str__(self):
        return f'Author: {author.fullname}, Quote: {quote}, tags: {tags}'
