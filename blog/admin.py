from django.contrib import admin
from .models import Article, ArticleTag, ArticleImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','id')
admin.site.register(Article)
admin.site.register(ArticleTag)
admin.site.register(ArticleImage)
