# Generated by Django 3.1 on 2020-11-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='sideways',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='friends',
            name='sideways',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lovelies',
            name='sideways',
            field=models.BooleanField(default=False),
        ),
    ]