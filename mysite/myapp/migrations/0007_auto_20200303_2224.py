# Generated by Django 3.0.3 on 2020-03-03 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200227_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestionmodel',
            name='image',
            field=models.ImageField(max_length=144, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='suggestionmodel',
            name='image_description',
            field=models.CharField(max_length=240, null=True),
        ),
    ]