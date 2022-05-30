from django.contrib import admin
from .models import Pump, Valley, Status


@admin.register(Valley)
class ValleyAdmin(admin.ModelAdmin):
    list_display = ['valley_name', 'valley_addr']

@admin.register(Pump)
class ValleyAdmin(admin.ModelAdmin):
    list_display = ['pump_name', 'pump_addr']


@admin.register(Status)
class ValleyAdmin(admin.ModelAdmin):
    list_display = ['status_valley', 'status_run', 'status_ctrl']
