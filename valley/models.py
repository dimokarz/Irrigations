from django.db import models
from surveillance.models import VideoSrv


class Pump(models.Model):
    class Meta:
        verbose_name = 'Насос'
        verbose_name_plural = 'Насосы'
        ordering = ['pk']

    pump_name = models.CharField(max_length=30, verbose_name='Название')
    pump_addr = models.CharField(max_length=15, verbose_name='Адрес')

    def __str__(self):
        return self.pump_name


class Valley(models.Model):
    class Meta:
        verbose_name = 'Система полива'
        verbose_name_plural = 'Системы полива'
        ordering = ['pk']

    valley_name = models.CharField(max_length=30, verbose_name='Название')
    valley_addr = models.CharField(max_length=15, verbose_name='Адрес')
    valley_pump = models.ForeignKey(Pump, on_delete=models.CASCADE, related_name='valley', verbose_name='Насос')
    valley_rele = models.SmallIntegerField(default=1, verbose_name='Реле')
    valley_duet = models.SmallIntegerField(default=0, verbose_name='Связка')
    valley_videosrv = models.ForeignKey(VideoSrv, on_delete=models.PROTECT, related_name='valley_cam',
                                        verbose_name='Видео сервер', null=True)
    valley_camera = models.CharField(max_length=100, verbose_name='Камера', null=True)


    def __str__(self):
        return self.valley_name


class Status(models.Model):
    class Meta:
        verbose_name = 'Состояние системы'
        verbose_name_plural = 'Состояния систем'
        ordering = ['pk']

    status_valley = models.OneToOneField(Valley, on_delete=models.CASCADE, primary_key=True,
                                         related_name='status', verbose_name='Система')
    status_run = models.BooleanField(default=False, verbose_name='Запущена')
    status_ctrl = models.BooleanField(default=False, verbose_name='Управление')
    status_fail = models.BooleanField(default=False, verbose_name='Авария')
    DIRECTIONS = [('N', '-'), ('F', 'Вперёд'), ('R', 'Назад')]
    status_dir = models.CharField(max_length=1, choices=DIRECTIONS, default='N', verbose_name='Направление')
    status_wat = models.BooleanField(default=False, verbose_name='Вода')
    status_sis = models.BooleanField(default=False, verbose_name='АвтоСтоп')
    status_valve1 = models.BooleanField(default=False, verbose_name='Задвижка 1')
    status_valve2 = models.BooleanField(default=False, verbose_name='Задвижка 2')
    status_perc = models.FloatField(default=False, verbose_name='Скорость')
    status_depth = models.FloatField(default=False, verbose_name='Глубина')
    status_start = models.DateTimeField(verbose_name='Время запуска')


class Journal(models.Model):

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

    journal_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    journal_valley = models.ForeignKey(Valley, on_delete=models.CASCADE, verbose_name='Система', null=True)
    journal_user = models.CharField(max_length=20, default='admin', verbose_name='Пользователь')
    ACTIONS = [('R', 'Запуск'), ('S', 'Остановка')]
    journal_act = models.CharField(max_length=1, choices=ACTIONS, default='S', verbose_name='Действия')
    DIRECTIONS = [('N', '-'), ('F', 'Вперёд'), ('R', 'Назад')]
    journal_dir = models.CharField(max_length=1, choices=DIRECTIONS, default='N', verbose_name='Направление')
    journal_wat = models.BooleanField(default=False, verbose_name='Вода')
    journal_sis = models.BooleanField(default=False, verbose_name='АвтоСтоп')
    journal_perc = models.FloatField(default=False, verbose_name='Скорость')
    journal_depth = models.FloatField(default=False, verbose_name='Глубина')
    journal_hours = models.FloatField(default=False, verbose_name='Время')