# Generated by Django 3.0.8 on 2020-08-15 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20200815_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='Insitute_city',
            new_name='Institute_city',
        ),
    ]