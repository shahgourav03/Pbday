# Generated by Django 3.1 on 2020-10-29 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201029_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='video',
        ),
    ]
