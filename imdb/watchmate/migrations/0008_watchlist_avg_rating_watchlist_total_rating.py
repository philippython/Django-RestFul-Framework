# Generated by Django 4.0 on 2022-08-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchmate', '0007_review_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='total_rating',
            field=models.IntegerField(default=0),
        ),
    ]
