# Generated by Django 4.0.5 on 2022-06-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveillance', '0002_alter_videosrv_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosrv',
            name='videosrv_http',
            field=models.IntegerField(max_length=10, null=True, verbose_name='Порт HTTP'),
        ),
        migrations.AddField(
            model_name='videosrv',
            name='videosrv_video',
            field=models.IntegerField(max_length=10, null=True, verbose_name='Порт видео'),
        ),
    ]
