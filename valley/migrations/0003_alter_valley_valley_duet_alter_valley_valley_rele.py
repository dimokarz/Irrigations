# Generated by Django 4.0.4 on 2022-05-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0002_valley_valley_duet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valley',
            name='valley_duet',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valley',
            name='valley_rele',
            field=models.SmallIntegerField(default=1),
        ),
    ]