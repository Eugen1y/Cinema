# Generated by Django 3.2.4 on 2021-06-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zal', '0003_auto_20210626_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='seans',
            name='price',
            field=models.IntegerField(default=10),
        ),
    ]
