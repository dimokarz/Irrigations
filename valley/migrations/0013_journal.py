# Generated by Django 4.0.5 on 2022-06-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0012_alter_valley_valley_camera_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jornal_date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
            ],
        ),
    ]