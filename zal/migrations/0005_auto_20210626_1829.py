# Generated by Django 3.2.4 on 2021-06-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zal', '0004_seans_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seans',
            name='datetime_end',
        ),
        migrations.RemoveField(
            model_name='seans',
            name='datetime_start',
        ),
        migrations.AddField(
            model_name='seans',
            name='date_end',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='seans',
            name='date_start',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='seans',
            name='time_end',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='seans',
            name='time_start',
            field=models.TimeField(auto_now=True),
        ),
    ]
