# Generated by Django 3.1 on 2020-10-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201015_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/myapp/images/'),
        ),
    ]
