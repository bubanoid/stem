# Generated by Django 3.1 on 2020-09-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='conducted',
            field=models.BooleanField(default=False, verbose_name='Відбулася'),
        ),
    ]
