# Generated by Django 3.1 on 2020-10-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_family_lovelies'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='video',
            field=models.FileField(null=True, upload_to='myapp/static/myapp/videos/', verbose_name=''),
        ),
    ]
