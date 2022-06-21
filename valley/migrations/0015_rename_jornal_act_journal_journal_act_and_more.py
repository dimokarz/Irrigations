# Generated by Django 4.0.5 on 2022-06-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valley', '0014_alter_journal_options_journal_jornal_act_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='jornal_act',
            new_name='journal_act',
        ),
        migrations.RenameField(
            model_name='journal',
            old_name='jornal_date',
            new_name='journal_date',
        ),
        migrations.CreateModel(
            name='JDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jdetails_dir', models.CharField(choices=[('N', '-'), ('F', 'Вперёд'), ('R', 'Назад')], default='N', max_length=1, verbose_name='Направление')),
                ('jdetails_wat', models.BooleanField(default=False, verbose_name='Вода')),
                ('jdetails_sis', models.BooleanField(default=False, verbose_name='АвтоСтоп')),
                ('jdetails_valve1', models.BooleanField(default=False, verbose_name='Задвижка 1')),
                ('jdetails_valve2', models.BooleanField(default=False, verbose_name='Задвижка 2')),
                ('jdetails_journal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='valley.journal', verbose_name='Строки')),
            ],
            options={
                'verbose_name': 'Запись журнала',
                'verbose_name_plural': 'Строки журнала',
            },
        ),
    ]
