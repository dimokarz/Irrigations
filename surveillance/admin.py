from django.contrib import admin
from .models import VideoSrv


@admin.register(VideoSrv)
class VideoSrvAdmin(admin.ModelAdmin):
    list_display = ['videosrv_name', 'videosrv_addr']
