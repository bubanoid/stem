from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Article
from events.models import Event

def main_page(request):
    latest_articles = Article.objects.order_by('-pub_date')[:3]
    random_articles = Article.objects.order_by('?')[:3]
    latest_events = Event.objects.order_by('-date')[:3]
    context = {
        'latest_article_list':latest_articles,
        'latest_events':latest_events,
        'random_articles':random_articles,
        }

    return render(request, 'main/home.html', context)

