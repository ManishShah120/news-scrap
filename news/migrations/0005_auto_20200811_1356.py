# Generated by Django 3.0.8 on 2020-08-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200811_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='datess',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
