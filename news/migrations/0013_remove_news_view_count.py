# Generated by Django 3.0.8 on 2020-09-07 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_news_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_count',
        ),
    ]