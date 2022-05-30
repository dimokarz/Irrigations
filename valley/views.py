from django.shortcuts import render
from django.http import HttpResponse
from .models import Valley, Status


def index(request):
    header = 'Выбор систем полива'
    title = ' - Выбор'
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all().values()
    return render(request, 'index.html', {'header': header, 'title': title, 'valley': valleyLst, 'status': statusLst})


def simple(request):
    header = 'Управление'
    title = ' - Управление'
    first = request.GET.get('first')
    second = request.GET.get('second')
    valLst = [first, second]

    return render(request, 'simple.html', {'header': header, 'title': title, 'valLst': valLst})


def test(request):
    valleyLst = Valley.objects.all().values()
    statusLst = Status.objects.all().values()
    t_lst = []
    for row in statusLst:
        valInd = int(row['status_valley_id'])
        valName = valleyLst.filter(id=valInd)
        row['valley_name'] = valName[0]['valley_name']
        t_lst.append(row)

    return render(request, 'test.html', {'res': t_lst})
