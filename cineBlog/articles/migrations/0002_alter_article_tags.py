# Generated by Django 4.2.3 on 2023-07-30 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.category'),
        ),
    ]
