# Generated by Django 4.0.4 on 2022-05-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0005_alter_pump_options_alter_status_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_dir',
            field=models.CharField(choices=[('N', '-'), ('F', 'Вперёд'), ('R', 'Назад')], default='N', max_length=1, verbose_name='Направление'),
        ),
    ]