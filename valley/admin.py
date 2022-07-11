from django.contrib import admin
from .models import Pump, Valley, Status, Journal


@admin.register(Valley)
class ValleyAdmin(admin.ModelAdmin):
    list_display = ['valley_name', 'valley_addr']

@admin.register(Pump)
class ValleyAdmin(admin.ModelAdmin):
    list_display = ['pump_name', 'pump_addr']


@admin.register(Status)
class ValleyAdmin(admin.ModelAdmin):
    list_display = ['status_valley', 'status_run', 'status_ctrl']

@admin.register(Journal)
class ValleyAdmin(admin.ModelAdmin):
    list_display = ['journal_date', 'journal_valley', 'journal_act', 'journal_perc', 'journal_depth', 'journal_hours']