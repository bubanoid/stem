# Generated by Django 3.1 on 2020-09-09 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20200909_1027'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cabinet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentHW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва домашнього завдання')),
                ('done_task', models.FileField(blank=True, null=True, upload_to='homeworks/', verbose_name='Домашнє завдання')),
                ('passed', models.BooleanField(default=False, verbose_name='Здано')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Домашня робота',
                'verbose_name_plural': 'Домашні роботи',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва предмету')),
                ('teacher', models.ManyToManyField(related_name='teachers', to='persons.Teacher')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предмети',
            },
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='ip',
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/group_logo', verbose_name='Лого групи'),
        ),
        migrations.DeleteModel(
            name='StudentIpAddress',
        ),
        migrations.AddField(
            model_name='studenthw',
            name='subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cabinet.subject'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='subjects',
            field=models.ManyToManyField(related_name='student_subjects', to='cabinet.Subject'),
        ),
    ]