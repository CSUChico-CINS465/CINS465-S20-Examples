# Generated by Django 3.0.3 on 2020-02-25 22:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0004_auto_20200213_2228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suggestion_Model',
            new_name='SuggestionModel',
        ),
    ]