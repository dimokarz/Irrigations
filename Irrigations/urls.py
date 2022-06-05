"""Irrigations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import valley.views

admin.site.site_header = 'Панель администратора'
admin.site.index_title = 'Администрирование систем полива и видеонаблюдения'

urlpatterns = [
    path('running/', valley.views.running),
    path('statussave/', valley.views.statussave),
    path('simple/', valley.views.simple),
    path('', valley.views.index),
    path('admin/', admin.site.urls),
]
