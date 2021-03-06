# Generated by Django 3.1 on 2020-09-14 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20200909_1027'),
        ('cabinet', '0004_studentschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentschedule',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.teacher', verbose_name='Викладач'),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='date',
            field=models.TimeField(verbose_name='Час уроку'),
        ),
    ]
