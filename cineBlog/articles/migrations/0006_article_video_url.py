# Generated by Django 4.2.4 on 2023-08-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_comments_related_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video_url',
            field=models.URLField(blank=True),
        ),
    ]
