# Generated by Django 4.0.4 on 2022-05-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0004_pump_duet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pump',
            name='duet',
        ),
        migrations.AddField(
            model_name='valley',
            name='duet',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
