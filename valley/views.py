import asyncio
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from urllib.request import urlopen
from xml.etree.ElementTree import parse
from .models import Valley, Status, Journal, Pump
from .control import ControlSimple, ControlFull
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
    btnLst = ControlSimple().rusButtons
    btnCol1 = ControlFull().rusButtons1
    btnCol2 = ControlFull().rusButtons2
    btnCol3 = ControlFull().rusButtons3
    btnCol4 = ControlFull().rusButtons4
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
    return render(request, 'simple.html', {'title': title, 'valleyLst': valleyLst, 'btnLst': btnLst, 'ptz': cam.ptz,
                                           'pCam': cam.pumpSub, 'vCam': cam.valleySub, 'journal': journal,
                                           'btnCol1': btnCol1, 'btnCol2': btnCol2, 'btnCol3': btnCol3,
                                           'btnCol4': btnCol4})


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
                      status_valve2=request.GET.get('valve2'), status_fail=request.GET.get('fail'),
                      status_perc=request.GET.get('perc'), status_depth=request.GET.get('dep'))
    currData.save()
    if request.GET.get('run') == 'False':
        act = 'S'
    else:
        act = 'R'
    currData = Journal(journal_valley=valleyId, journal_act=act, journal_user=request.user.get_username(),
                       journal_dir=request.GET.get('dir'), journal_wat=request.GET.get('wat'),
                       journal_sis=request.GET.get('sis'), journal_perc=request.GET.get('perc'),
                       journal_depth=request.GET.get('dep'))
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


def valrele(request):
    contr = request.GET.get('contr')
    rele = request.GET.get('rele')
    stat = request.GET.get('status')
    if contr == '5':
        addr = '192.168.1.151'
    elif contr == '6':
        addr = '192.168.1.109'
    return HttpResponse(lauRele(addr, rele, stat))


def minijourn(request):
    first = request.GET.get('first')
    if request.GET.get('second') is not None:
        second = request.GET.get('second')
        journal = Journal.objects.all().filter(journal_valley__in=(first, second)).order_by('-journal_date')[:7]
    else:
        journal = Journal.objects.all().filter(journal_valley=first).order_by('-journal_date')[:7]
    return render(request, 'minijourn.html', {'journal': journal})


def currec(request):
    curr = request.GET.get('curr')
    detail = Journal.objects.all().filter(journal_valley_id=int(curr))
    return HttpResponse(detail)


def journlst(request):
    return render(request, 'journlst.html')


def journal(request):
    journ = Journal.objects.all().order_by('-journal_date')
    return render(request, 'journal.html', {'journLst': journ})


def journfilt(request):
    pass


def test(request):
    return render(request, 'test.html')


# def lauin(request):
#     contr = request.GET.get('contr')
#     str_url = 'http://192.168.1.107/state.xml'
#     lauXml = urlopen(str_url)
#     xmldoc = parse(lauXml)
#     inputs = xmldoc.findtext('in')
#     return HttpResponse(inputs[0])

def lauin(request):
    contr = request.GET.get('contr')
    str_url = 'http://192.168.1.107/state.xml'  # !!!!!
    lauXml = urlopen(str_url)
    xmldoc = parse(lauXml)
    inputs = xmldoc.findtext('in')
    if int(contr) == 6:
        valv1 = inputs[0]  # !!!!!
        str_url = 'http://192.168.1.109/json_sensor.cgi?psw=Laurent'  # !!!!!
    elif int(contr) == 5:
        valv1 = inputs[0]  # !!!!!
        str_url = 'http://192.168.1.151/json_sensor.cgi?psw=Laurent'  # !!!!!
    jData = requests.get(str_url, verify=False)
    inputs = json.loads(jData.text)
    valv2 = inputs['in'][1]  # !!!!!
    if int(valv1) == 1 and int(valv2) == 1:
        valv = 1
    else:
        valv = 0
    print(valv1, valv2, valv)
    print(str_url)
    return HttpResponse(str(valv))


def listenin(request):
    contr = request.GET.get('contr')
    valStat = request.GET.get('stat')

    if int(contr) == 5:
        contrAddr = '192.168.1.251'
    elif int(contr) == 6:
        contrAddr = '192.168.1.108'

    # print('valStat=' + valStat)
    if int(valStat) == 1:
        pin1Rele(contrAddr, 44, 1)  # !!!!!
    elif int(valStat) == 0:
        pin1Rele(contrAddr, 44, 0)  # !!!!!
    return HttpResponse(contrAddr + ' ' + str(contr) + ' ' + str(valStat))


# async def stimer(request):
#     await asyncio.sleep(5)
#     return HttpResponse('Ебеньк')


def onoff(request):
    contr = request.GET.get('contr')
    if int(contr) == 5:
        contrAddr = 'http://192.168.1.151/json_sensor.cgi?psw=Laurent'
    elif int(contr) == 6:
        contrAddr = 'http://192.168.1.109/json_sensor.cgi?psw=Laurent'

    jData = requests.get(contrAddr, verify=False)
    inputs = json.loads(jData.text)
    valState = inputs['rele'][0]
    return HttpResponse(valState)
