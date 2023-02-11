from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from .forms import FormQuote
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
    # author = Authors.objects.filter(fullname=author_here).first()
    # author = Authors.objects.get(fullname=author_id)
    author = get_object_or_404(Authors, pk=author_here)

    return render(request, 'app_quotes/author_single.html', context={"author": author})


def def_tag_clic(request, recived_tag):
    quotes_w_tag = Quotes.objects.filter(tags__contains=[str(recived_tag)])
    # quotes_w_tag = str(recived_tag)
    return render(request, 'app_quotes/quote_by_tag.html', context={'quotes_w_tag': quotes_w_tag})


@login_required
def def_add_quote(request):
    if request.method == 'POST':
        data_form = FormQuote(request.POST)

        if data_form.is_valid():

            try:
                check_auth = Quotes.objects.get(fullname=request.POST.author)

            except Quotes.DoesNotExist:
                Authors(fullname=request.POST.author).save()
                new_quote = data_form.save()

            parce_tags = data_form.tags.split(",", 3)
            print(parce_tags)
            new_quote.tags.add(parce_tags)
            print('tags saved')

            return redirect(to='app_quotes:main')
        else:
            return render(request, 'app_quotes/failure.html')

    return render(request, 'app_quotes/add_quote.html', {'form': FormQuote()})
