# Generated by Django 4.0.4 on 2022-05-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSrv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videosrv_name', models.CharField(max_length=30, verbose_name='Название')),
                ('videosrv_addr', models.CharField(max_length=15, verbose_name='Адрес')),
                ('videosrv_user', models.CharField(max_length=15)),
                ('videosrv_password', models.CharField(max_length=30)),
            ],
        ),
    ]
