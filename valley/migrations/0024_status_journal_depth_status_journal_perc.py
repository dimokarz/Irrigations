# Generated by Django 4.0.6 on 2022-07-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0023_alter_journal_journal_depth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='journal_depth',
            field=models.FloatField(default=False, verbose_name='Глубина'),
        ),
        migrations.AddField(
            model_name='status',
            name='journal_perc',
            field=models.FloatField(default=False, verbose_name='Скорость'),
        ),
    ]