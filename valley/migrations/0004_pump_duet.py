# Generated by Django 4.0.4 on 2022-05-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0003_alter_vall_status_dir'),
    ]

    operations = [
        migrations.AddField(
            model_name='pump',
            name='duet',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]