# Generated by Django 3.1 on 2020-10-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='myapp/static/myapp/videos/'),
        ),
    ]
