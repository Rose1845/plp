from multiprocessing import context

from django.shortcuts import render
from .models import Article,ArticleSeries
# Create your views here.s
def homepage(request):
    matching_series = ArticleSeries.objects.all()
    return render(request=request,
    template_name = 'main/home.html',
    context ={"objects":matching_series})
# series
def series(request,series:str  ):
    matching_series = ArticleSeries.objects.filter(slug=series).all()
    return render(request=request,
    template_name = 'main/home.html',
    context ={"objects":matching_series})

    # article
def article(request,series:str ,article:str ):
    matching_article = Article.objects.filter(series=series,article_slug=article).first()
    return render(request=request,
    template_name = 'main/article.html',
    context ={"objects":matching_article})