from django.shortcuts import render
from django.http import HttpResponse
from .models import Valley, Status
from .control import ControlSimple
from surveillance.trassir import *


def index(request):
    header = 'Выбор систем полива'
    title = ' - Выбор'
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all()
    return render(request, 'index.html', {'header': header, 'title': title, 'valley': valleyLst, 'status': statusLst})


def simple(request):
    cam = camera()
    btnLst = ControlSimple().rusButtons
    first = int(request.GET.get('first')[5:])
    if request.GET.get('second') is not None:
        second = request.GET.get('second')[5:]
        valleyLst = Status.objects.all().in_bulk([first, second]).values()
    else:
        valleyLst = Status.objects.all().in_bulk([first]).values()
    title = ' - Управление'
    return render(request, 'simple.html', {'title': title, 'valleyLst': valleyLst, 'btnLst': btnLst, 'cam': cam[0]})


def whichrun(request):
    running = []
    statusLst = Status.objects.all().values()
    for run in statusLst:
        if run['status_run'] == True:
            running.append(run['status_valley_id'])
    return HttpResponse(running)


def statussave(request):
    valleyId = Valley.objects.get(id=request.GET.get('id'))
    currData = Status(status_valley=valleyId, status_ctrl=True, status_run=request.GET.get('run'),
                      status_dir=request.GET.get('dir'), status_wat=request.GET.get('wat'),
                      status_sis=request.GET.get('sis'), status_valve1=request.GET.get('valve1'),
                      status_valve2=request.GET.get('valve2'))
    currData.save()
    return HttpResponse('Ok')
