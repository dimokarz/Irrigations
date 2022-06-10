// Проверка выбранных систем
function btn_sel() {
    let duet = []
    let valley = []
    let inputElems = document.getElementsByTagName("input"),
    count = 0;

    for (let i = 0; i < inputElems.length; i++) {
        if (inputElems[i].type == "checkbox" && inputElems[i].checked == true) {
            count++;
            duet.push(inputElems[i].value)
            valley.push(inputElems[i].id)
        }
    }
    switch (count) {
        case 1:
            window.open("/simple?first=" + valley[0], "_self")
            break;
        case 2:
            if (duet[0] == duet[1] && duet[0] != 0) {
                window.open("/simple?first=" + valley[0] + "&second=" + valley[1], "_self")
            }
            else {
                $('#mal1').text("Выбранные системы не могут работать в паре");
                $('#modAlert').modal("show");
            }
            break;
        default:
            $('#mal1').text("Вы можете выбрать не более двух систем");
            $('#modAlert').modal("show");
            break;
    }
}

// Всплывашки
function toastInit(stat, tmess) {
    $('#tHead').addClass(stat);
    $('#tMess1').text(tmess);
    $('.toast').toast('show');
};


//Сохранение статуса систем
function dataSave() {
    $.ajax({
        url: '/statussave/',
        type: 'GET',
        dataType: 'json',
        data: valStatus,
    });
};

//Изменение цвета индикаторов
function indEdit(currInd = 'All', removeClass, addClass) {
    if (currInd == 'All') {
        $('#dirInd' + valleyNumber).removeClass(removeClass);
        $('#dirInd' + valleyNumber).addClass(addClass);
        $('#watInd' + valleyNumber).removeClass(removeClass);
        $('#watInd' + valleyNumber).addClass(addClass);
        $('#sisInd' + valleyNumber).removeClass(removeClass);
        $('#sisInd' + valleyNumber).addClass(addClass);
        $('#valve1' + valleyNumber).removeClass(removeClass);
        $('#valve1' + valleyNumber).addClass(addClass);
        $('#valve2' + valleyNumber).removeClass(removeClass);
        $('#valve2' + valleyNumber).addClass(addClass);
    }
    else {
        $('#' + currInd + valleyNumber).removeClass(removeClass);
        $('#' + currInd + valleyNumber).addClass(addClass);
    }
}

//Открытие запущенных систем
function witchRun() {
    $.ajax({
        url: '/whichrun/',
        type: 'GET',
        success: function (data) {
            switch (data.length) {
                case 1:
                    window.open("/simple?first=v_chk" + data[0], "_self");
                    break;
                case 2:
                    window.open("/simple?first=v_chk" + data[0] + "&second=v_chk" + data[1], "_self");
                    break;
                default:
                    $('#mal1').text("Ни одна система не запущена");
                    $('#modAlert').modal("show");
                    break;
            }
        }
    });
}

// Окно контроля запуска
function startInit() {
    $('#pValve1').text('Открытие первой задвижки...')
    $('#pValve1').removeClass('text-success')
    $('#pValve1').removeClass('fw-bold')
    $('#pValve1').addClass('text-body')
    $('#spValve1').show()

    $('#pPump1').text('Запуск первого насоса...')
    $('#pPump1').removeClass('text-success')
    $('#pPump1').removeClass('fw-bold')
    $('#pPump1').addClass('text-secondary')
    $('#spPump1').hide()
    $('#irrigOn').modal('show')

    $('#pValve2').text('Открытие второй задвижки...')
    $('#pValve2').removeClass('text-success')
    $('#pValve2').removeClass('fw-bold')
    $('#pValve2').addClass('text-secondary')
    $('#spValve2').hide()

    $('#pPump2').text('Запуск второго насоса...')
    $('#pPump2').removeClass('text-success')
    $('#pPump2').removeClass('fw-bold')
    $('#pPump2').addClass('text-secondary')
    $('#spPump2').hide()

    $('#irrigOn').modal('show')

    setTimeout(function(){
        $('#spValve1').hide()
        $('#pValve1').removeClass('text-body');
        $('#pValve1').addClass('text-success');
        $('#pValve1').addClass('fw-bold');
        $('#pValve1').text('Первая задвижка открыта');
        $('#spPump1').show()
        $('#pPump1').removeClass('text-secondary')
        $('#pPump1').addClass('text-body')
        valStatus.valve1 = 'True'
    }, 2000);

    setTimeout(function () {
        $('#spPump1').hide()
        $('#pPump1').removeClass('text-body');
        $('#pPump1').addClass('text-success');
        $('#pPump1').addClass('fw-bold');
        $('#pPump1').text('Первый насос запущен');
        $('#spValve2').show()
        $('#pValve2').removeClass('text-secondary')
        $('#pValve2').addClass('text-body')
    }, 4000);

    setTimeout(function(){
        $('#spValve2').hide()
        $('#pValve2').removeClass('text-body');
        $('#pValve2').addClass('text-success');
        $('#pValve2').addClass('fw-bold');
        $('#pValve2').text('Вторая задвижка открыта');
        $('#spPump2').show()
        $('#pPump2').removeClass('text-secondary')
        $('#pPump2').addClass('text-body')
        valStatus.valve2 = 'True'
    }, 6000);

    setTimeout(function () {
        $('#spPump2').hide()
        $('#pPump2').removeClass('text-body');
        $('#pPump2').addClass('text-success');
        $('#pPump2').addClass('fw-bold');
        $('#pPump2').text('Второй насос запущен');
        indEdit('dirInd','bg-danger', 'bg-success')
        indEdit('watInd','bg-danger', 'bg-success')
        indEdit('valve1','bg-danger', 'bg-success')
        indEdit('valve2','bg-danger', 'bg-success')
    }, 8000);

    setTimeout(function () {
        $('#irrigOn').modal('hide')
        toastInit('bg-success', 'Система запущена с подачей воды');
    }, 10000);



}