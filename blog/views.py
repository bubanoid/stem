from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from .models import Article

class ArticlesView(View):
    def get(self, request):
        latest_article_list = Article.objects.order_by('-pub_date')[:2000]
        context = {'latest_article_list':latest_article_list}
        return render(request, 'blog/blog.html', context)


class DetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug = slug)
        return render(request, 'blog/detail.html', {'article':article})

def about(request):
    return render(request, 'blog/about.html')


