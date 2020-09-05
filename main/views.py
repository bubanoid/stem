from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Article

def main_page(request):
    latest_articles = Article.objects.order_by('-pub_date')[:3]
    context = {'latest_article_list':latest_articles}

    return render(request, 'main/home.html', context)
