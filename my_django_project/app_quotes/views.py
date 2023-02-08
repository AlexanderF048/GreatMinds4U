from django.shortcuts import render, get_object_or_404
from .models import Authors, Quotes


# Create your views here.
def main(request):
    return render(request, 'app_quotes/index.html', context={"name_page": "Main page"})


def def_quotes(request):
    quotes_db = Quotes.objects.all()
    return render(request, 'app_quotes/quotes.html', context={"quotes_db": quotes_db})


def def_authors(request):
    authors_db = Authors.objects.all()
    return render(request, 'app_quotes/authors.html', context={"authors_db": authors_db})


def def_author_single(request, author_here):
    #author = Authors.objects.filter(fullname=author_here).first()
    #author = Authors.objects.get(fullname=author_id)
    author = get_object_or_404(Authors, pk=author_here)

    return render(request, 'app_quotes/author_single.html', context={"author": author})
