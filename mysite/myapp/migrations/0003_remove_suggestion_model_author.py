# Generated by Django 3.0.2 on 2020-02-06 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_suggestion_model_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion_model',
            name='author',
        ),
    ]
