# Generated by Django 4.0.6 on 2022-07-28 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0024_status_journal_depth_status_journal_perc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='journal_depth',
            new_name='status_depth',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='journal_perc',
            new_name='status_perc',
        ),
    ]
