from django.contrib import admin
from .models import Article, ArticleTag, ArticleImage

admin.site.register(Article)
admin.site.register(ArticleTag)
admin.site.register(ArticleImage)
