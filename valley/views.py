from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Valley, Status
from .control import ControlSimple
from .arduino import *
from surveillance.trassir import *


@login_required
def index(request):
    header = 'Выбор систем полива'
    title = ' - Выбор'
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all()
    return render(request, 'index.html', {'header': header, 'title': title, 'valley': valleyLst, 'status': statusLst})


@login_required
def simple(request):
    btnLst = ControlSimple().rusButtons
    first = int(request.GET.get('first')[5:])
    if request.GET.get('second') is not None:
        second = request.GET.get('second')[5:]
        valleyLst = Status.objects.all().in_bulk([first, second]).values()
        cam = VideoUrl(first, second)
    else:
        valleyLst = Status.objects.all().in_bulk([first]).values()
        cam = VideoUrl(first, 0)
    title = ' - Управление'
    return render(request, 'simple.html', {'title': title, 'valleyLst': valleyLst, 'btnLst': btnLst,
                                           'pCam': cam.pumpSub, 'vCam': cam.valleySub, 'vCamMain': cam.valleyMain})

@login_required
def whichrun(request):
    running = []
    statusLst = Status.objects.all().values()
    for run in statusLst:
        if run['status_run']:
            running.append(run['status_valley_id'])
    return HttpResponse(running)

@login_required
def statussave(request):
    valleyId = Valley.objects.get(id=request.GET.get('id'))
    currData = Status(status_valley=valleyId, status_ctrl=True, status_run=request.GET.get('run'),
                      status_dir=request.GET.get('dir'), status_wat=request.GET.get('wat'),
                      status_sis=request.GET.get('sis'), status_valve1=request.GET.get('valve1'),
                      status_valve2=request.GET.get('valve2'))
    currData.save()
    return HttpResponse('Ok')

@login_required
def btnclick(request):
    addr = Valley.objects.get(id=request.GET.get('contr')).valley_addr
    rele1 = request.GET.get('rele1')
    rele1 = int(rele1) + 30
    rele2 = request.GET.get('rele2')
    rele2 = int(rele2) + 30
    ttt = str(rele1) + '-' + str(rele2)
    return HttpResponse(pin2Rele(addr, rele1, rele2))

@login_required
def singlerele(request):
    addr = Valley.objects.get(id=request.GET.get('contr')).valley_addr
    rele = request.GET.get('rele')
    rele = int(rele) + 30
    status = request.GET.get('status')
    return HttpResponse(pin1Rele(addr, rele, status))

def readpin(request):
    addr = Valley.objects.get(id=request.GET.get('contr')).valley_addr
    pin = request.GET.get('pin')
    return HttpResponse(pinInput(addr, pin))
