from django.shortcuts import render
from .models import Valley, Status
from .control import ControlSimple


def index(request):
    header = 'Выбор систем полива'
    title = ' - Выбор'
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all()
    return render(request, 'index.html', {'header': header, 'title': title, 'valley': valleyLst, 'status': statusLst})


def simple(request):
    btnLst = ControlSimple().rusButtons
    first = int(request.GET.get('first')[5:])
    if request.GET.get('second') is not None:
        second = request.GET.get('second')[5:]
        valleyLst = Status.objects.all().in_bulk([first, second]).values()
    else:
        valleyLst = Status.objects.all().in_bulk([first]).values()
    title = ' - Управление'

    return render(request, 'simple.html', {'title': title, 'valleyLst': valleyLst, 'btnLst': btnLst})


def test(request):
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all().values()
    btnLst = ControlSimple().rusButtons

    return render(request, 'test.html', {'btnLst': btnLst, 'valleyLst': valleyLst, 'statusLst': statusLst})
