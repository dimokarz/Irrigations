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
function startInit(btn) {
    $('#pValve').text('Открытие задвижек...')
    $('#pValve').removeClass('text-success')
    $('#pValve').addClass('text-body')
    $('#spValve').show()

    $('#pPump').text('Запуск насоса...')
    $('#pPump').removeClass('text-success')
    $('#pPump').addClass('text-secondary')
    $('#spPump').hide()

    $('#pSystem').text('Запуск системы...')
    $('#pSystem').removeClass('text-success')
    $('#pSystem').addClass('text-secondary')
    $('#spSystem').hide()

    $('.progress-bar').css('width', '0%');

    $('#irrigOn').modal('show')

    setTimeout(function(){
        $('#spValve').hide()
        $('#pValve').removeClass('text-body');
        $('#pValve').addClass('text-success');
        $('#pValve').text('Задвижки открыты');
        $('#spPump').show()
        $('#pPump').removeClass('text-secondary')
        $('#pPump').addClass('text-body')
        indEdit('valve1','bg-danger', 'bg-success')
        indEdit('valve2','bg-danger', 'bg-success')
        $('.progress-bar').css('width', '50%');
    }, 2000);

    setTimeout(function () {
        $('#spPump').hide()
        $('#pPump').removeClass('text-body');
        $('#pPump').addClass('text-success');
        $('#pPump').text('Насос запущен');
        indEdit('dirInd','bg-danger', 'bg-success')
        $('#spSystem').show()
        $('#pSystem').removeClass('text-secondary')
        $('#pSystem').addClass('text-body')
        $('.progress-bar').css('width', '75%')
    }, 3000);

    setTimeout(function(){
        $('#spSystem').hide()
        $('#pSystem').removeClass('text-body');
        $('#pSystem').addClass('text-success');
        $('#pSystem').text('Система запущена');
        indEdit('watInd','bg-danger', 'bg-success')
        $('#spSystem').show()
        // $('#pSystem').removeClass('text-secondary')
        // $('#pSystem').addClass('text-body')
        $('.progress-bar').css('width', '100%');
    }, 4000);

    setTimeout(function () {
        $('#irrigOn').modal('hide')
        reqRele('btn' + valleyNumber + '_7-9')
    }, 5000);

    setTimeout(function () {
        toastInit('bg-success', 'Система запущена с подачей воды');
    }, 6000);
};


function reqRele(btnClick) {
    let url = '/btnclick/?contr=' + btnClick.slice(3, 4)  + '&rele1=' + btnClick.slice(5, 6) + '&rele2=' + btnClick.slice(7)
    btnDisable(true, btnClick.slice(3, 4))
    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            if (response != 'False') {
                btnEnable(true, btnClick.slice(3, 4))
            }
        }
    });
}

function btnDisable(all= false, btn= 0) {
    if (all == false) {
        $('#' + btn).prop("disabled", true);
    }
    else {
        $('#btn' + btn + '_7-9').prop("disabled", true);
        $('#btn' + btn + '_8-9').prop("disabled", true);
        $('#btn' + btn + '_7-10').prop("disabled", true);
        $('#btn' + btn + '_8-10').prop("disabled", true);
        $('#btn' + btn + '_7-11').prop("disabled", true);
        $('#btn' + btn + '_8-11').prop("disabled", true);
        $('#btn' + btn + '_7-12').prop("disabled", true);
        $('#btn' + btn + '_8-12').prop("disabled", true);
    }
}

function btnEnable(all = false, btn = 0) {
    if (all == false) {
        $('#' + btn).prop("disabled", false);
    }
    else {
        $('#btn' + btn + '_7-9').prop("disabled", false);
        $('#btn' + btn + '_8-9').prop("disabled", false);
        $('#btn' + btn + '_7-10').prop("disabled", false);
        $('#btn' + btn + '_8-10').prop("disabled", false);
        $('#btn' + btn + '_7-11').prop("disabled", false);
        $('#btn' + btn + '_8-11').prop("disabled", false);
        $('#btn' + btn + '_7-12').prop("disabled", false);
        $('#btn' + btn + '_8-12').prop("disabled", false);
    }
}