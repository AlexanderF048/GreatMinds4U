from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.core.paginator import Paginator

from .forms import FormQuote
from .models import Authors, Quotes


# Можно через классы а не функции from django.views import View и передавать View
# Create your views here.
def main(request):
    return render(request, 'app_quotes/index.html', context={"name_page": "Main page"})


def def_quotes(request):


    quotes_db = Quotes.objects.all()

    paginator = Paginator(quotes_db, 3, orphans=3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_quotes/quotes.html', context={"quotes_db": quotes_db, "page_object": page_obj})


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
        tags_list = request.POST.get('tags').split(',', 5)

        if data_form.is_valid():
            try:
                check_auth = Authors.objects.get(fullname=request.POST.get('author'))
                new_quote = data_form.save(commit=False)
                new_quote.author = check_auth
                new_quote.tags = [tag.strip() for tag in tags_list]
                new_quote.save()

            except Authors.DoesNotExist:
                new_author = Authors(fullname=request.POST['author']).save()

                new_quote = data_form.save(commit=False)
                new_quote.author = Authors.objects.get(fullname=request.POST.get('author'))
                new_quote.tags = [tag.strip() for tag in tags_list]
                new_quote.save()

            return redirect(to='app_quotes:main')
        else:
            return render(request, 'app_quotes/failure.html')

    return render(request, 'app_quotes/add_quote.html', {'form': FormQuote()})
