from django.db import models


class VideoSrv(models.Model):

    class Meta:
        verbose_name = 'Видео сервер'
        verbose_name_plural = 'Видео серверы'
        ordering = ['pk']

    videosrv_name = models.CharField(max_length=30, verbose_name='Название')
    videosrv_addr = models.CharField(max_length=15, verbose_name='Адрес')
    videosrv_user = models.CharField(max_length=15, verbose_name='Пользователь')
    videosrv_password = models.CharField(max_length=30, verbose_name='Пароль')

    def __str__(self):
        return self.videosrv_name
