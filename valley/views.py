from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from urllib.request import urlopen
from xml.etree.ElementTree import parse
from .models import Valley, Status, Journal, Pump
from .control import ControlSimple
from .arduino import *
from surveillance.trassir import *
from .laurent import *


@login_required
def index(request):
    header = 'Выбор систем полива'
    title = ' - Выбор'
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all()
    return render(request, 'index.html', {'header': header, 'title': title, 'valley': valleyLst, 'status': statusLst})


@login_required
def simple(request):
    btnLst = ControlSimple().engButtons
    first = int(request.GET.get('first')[5:])
    if request.GET.get('second') is not None:
        second = request.GET.get('second')[5:]
        valleyLst = Status.objects.all().in_bulk([first, second]).values()
        try:
            cam = VideoUrl(first, second)
        except:
            cam = ''
        journal = Journal.objects.all().filter(journal_valley__in=(first, second)).order_by('-journal_date')[:7]
    else:
        valleyLst = Status.objects.all().in_bulk([first]).values()
        try:
            cam = VideoUrl(first, 0)
        except:
            cam = ''
        journal = Journal.objects.all().filter(journal_valley=first).order_by('-journal_date')[:7]
    title = ' - Управление'
    # return render(request, 'simple.html', {'title': title, 'valleyLst': valleyLst, 'btnLst': btnLst,
    #                                        'pCam': cam.pumpMain, 'vCam': cam.valleyMain, 'pSids': cam.getSid,
    #                                        'journal': journal})
    return render(request, 'simple.html', {'title': title, 'valleyLst': valleyLst, 'btnLst': btnLst,
                                           'journal': journal})


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
                      status_valve2=request.GET.get('valve2'), status_fail=request.GET.get('fail'))
    currData.save()
    if request.GET.get('run') == 'False':
        act = 'S'
    else:
        act = 'R'
    currData = Journal(journal_valley=valleyId, journal_act=act, journal_user=request.user.get_username(),
                       journal_dir=request.GET.get('dir'), journal_wat=request.GET.get('wat'),
                       journal_sis=request.GET.get('sis'))
    currData.save()
    return HttpResponse('Ok')


@login_required
def btnclick(request):
    addr = Valley.objects.get(id=request.GET.get('contr')).valley_addr
    rele1 = request.GET.get('rele1')
    rele1 = int(rele1) + 30
    rele2 = request.GET.get('rele2')
    rele2 = int(rele2) + 30
    return HttpResponse(pin2Rele(addr, rele1, rele2))


@login_required
def singlerele(request):
    addr = Valley.objects.get(id=request.GET.get('contr')).valley_addr
    rele = request.GET.get('rele')
    rele = int(rele) + 30
    status = request.GET.get('status')
    return HttpResponse(pin1Rele(addr, rele, status))


@login_required
def readpin(request):
    addr = Valley.objects.get(id=request.GET.get('contr')).valley_addr
    pin = request.GET.get('pin')
    return HttpResponse(pinInput(addr, pin))


def laurele(request):
    contr = Valley.objects.get(id=request.GET.get('contr'))
    addr = Pump.objects.get(id=contr.valley_pump_id).pump_addr
    rele = contr.valley_rele
    stat = request.GET.get('status')
    return HttpResponse(lauRele(addr, rele, stat))


def minijourn(request):
    first = request.GET.get('first')
    if request.GET.get('second') is not None:
        second = request.GET.get('second')
        journal = Journal.objects.all().filter(journal_valley__in=(first, second)).order_by('-journal_date')[:7]
    else:
        journal = Journal.objects.all().filter(journal_valley=first).order_by('-journal_date')[:7]
    return render(request, 'minijourn.html', {'journal': journal})


def journlst(request):
    return render(request, 'journlst.html')


def journal(request):
    journ = Journal.objects.all().order_by('-journal_date')
    return render(request, 'journal.html', {'journLst': journ})


def journfilt(request):
    pass


def test(request):
    return render(request, 'test.html')


def lauin(request):
    contr = request.GET.get('contr')
    str_url = 'http://192.168.1.107/state.xml'
    lauXml = urlopen(str_url)
    xmldoc = parse(lauXml)
    inputs = xmldoc.findtext('in')
    ### Температура
    result = round(float(xmldoc.findtext('temp')), 1)
    return HttpResponse(inputs[0])
