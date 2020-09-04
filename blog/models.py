from django.db import models
from django.utils import timezone
import datetime

class ArticleTag(models.Model):
    tag = models.CharField('Тег', max_length=200)
    class Meta:
        verbose_name = 'Тег для статті'
        verbose_name_plural = 'Теги для статтей'
    
    def __str__(self):
        return self.tag


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Назва статті', max_length=200)
    text = models.TextField('Текст статті')
    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)
    article_tag = models.ManyToManyField(ArticleTag, related_name='Теги')
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    image2 = models.ImageField(upload_to='blog/', blank=True, null=True)
    image3 = models.ImageField(upload_to='blog/', blank=True, null=True)
    image3 = models.ImageField(upload_to='blog/', blank=True, null=True)
    slug = models.SlugField('Посилання', max_length=50)

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    title = models.CharField('Короткий опис картинки', max_length=50)
    image = models.ImageField('Картинка', upload_to='article_images/')
    article = models.ForeignKey(Article, verbose_name='Стаття', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Картинка статті'
        verbose_name_plural = 'Картинки статті'
    