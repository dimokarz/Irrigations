from django.shortcuts import render
from django.http import HttpResponse
from .models import Valley, Status
from .control import ControlBtn


def index(request):
    header = 'Выбор систем полива'
    title = ' - Выбор'
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all()
    return render(request, 'index.html', {'header': header, 'title': title, 'valley': valleyLst, 'status': statusLst})


def simple(request):
    first = int(request.GET.get('first')[5:])
    if request.GET.get('second') is not None:
        second = request.GET.get('second')[5:]
        valleyLst = Status.objects.all().in_bulk([first, second]).values()
    else:
        valleyLst = Status.objects.all().in_bulk([first]).values()
    header = 'Управление'
    title = ' - Управление'

    return render(request, 'simple.html', {'header': header, 'title': title, 'valleyLst': valleyLst})


def test(request):
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all().values()
    btnLst = ControlBtn().rusButtons

    return render(request, 'test.html', {'btnLst': btnLst, 'valleyLst': valleyLst, 'statusLst': statusLst})
