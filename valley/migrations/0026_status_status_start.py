# Generated by Django 4.0.6 on 2022-08-03 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0025_rename_journal_depth_status_status_depth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='status_start',
            field=models.DateTimeField(auto_now=True, verbose_name='Время запуска'),
        ),
    ]
