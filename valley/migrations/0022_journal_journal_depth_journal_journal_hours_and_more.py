# Generated by Django 4.0.6 on 2022-07-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0021_alter_valley_valley_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='journal_depth',
            field=models.SmallIntegerField(default=False, verbose_name='Depth'),
        ),
        migrations.AddField(
            model_name='journal',
            name='journal_hours',
            field=models.SmallIntegerField(default=False, verbose_name='Hourse'),
        ),
        migrations.AddField(
            model_name='journal',
            name='journal_perc',
            field=models.SmallIntegerField(default=False, verbose_name='Percent'),
        ),
    ]
