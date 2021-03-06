# Generated by Django 3.1 on 2020-08-26 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва статті')),
                ('text', models.TextField(verbose_name='Текст статті')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')),
                ('slug', models.SlugField(verbose_name='Посилання')),
            ],
            options={
                'verbose_name': 'Стаття',
                'verbose_name_plural': 'Статті',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/blog', verbose_name='Картинка для статті')),
            ],
            options={
                'verbose_name': 'Картинка для статті',
                'verbose_name_plural': 'Картинки для статтей',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег для статті',
                'verbose_name_plural': 'Теги для статтей',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(help_text='Короткий опис питання', max_length=100, verbose_name='Назва питання')),
                ('question_text', models.CharField(max_length=200, verbose_name='Текст запитання про статтю')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
            options={
                'verbose_name': 'Питання',
                'verbose_name_plural': 'Питання',
            },
        ),
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=100, verbose_name='Варіант відповіді')),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.question')),
            ],
            options={
                'verbose_name': 'Варіант',
                'verbose_name_plural': 'Варіанти',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(related_name='Теги', to='blog.ArticleTag'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ManyToManyField(related_name='Картинки', to='blog.ArticleImage'),
        ),
    ]
