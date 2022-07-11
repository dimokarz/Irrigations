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

//Чтение входов Laurent
function lauStatus(contr) {
    let url = '/lauin/?contr=' + contr
    $.ajax({
        url: url,
        type: 'GET',
        success: function (request) {
            lauInp = request
        }
    })
    return lauInp
}

//Контроль открытия задвижки и запуска
function valveOpen(contr) {
        let interval2 = setInterval(function () {
            if (lauStatus(vallRun) == 1) {
    // Открытие задвижек
                $('#spValve').hide()
                $('#pValve').removeClass('text-body');
                $('#pValve').addClass('text-success');
                $('#pValve').text('Задвижки открыты');
                $('#spPump').show()
                $('#pPump').removeClass('text-secondary')
                $('#pPump').addClass('text-body')
                indEdit('valve1','bg-danger', 'bg-success')
                indEdit('valve2','bg-danger', 'bg-success')
                $('.progress-bar').css('width', '75%');
   // Запуск насосса
                setTimeout(function () {
                    $('#spPump').hide()
                    $('#pPump').removeClass('text-body');
                    $('#pPump').addClass('text-success');
                    $('#pPump').text('Насос запущен');
                    indEdit('dirInd', 'bg-danger', 'bg-success')
                    $('#spSystem').show()
                    $('#pSystem').removeClass('text-secondary')
                    $('#pSystem').addClass('text-body')
                    $('.progress-bar').css('width', '75%')
                }, 2000);
                clearInterval(interval2)
    // Запуск систем
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
                    $('#startProgr').css('display', 'none');
                    $('#modCam').modal("hide")
                    sinRele(vallRun, 14, 1)
                    reqRele('btn' + valleyNumber + '_7-9')
                }, 6000);
                setTimeout(function () {
                    toastInit('bg-success', 'Система запущена с подачей воды');
                }, 7000)
            }
        }, 1000)
    lauInp = 0
}

// Окно контроля запуска
function startInit(cntr) {
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

    // $('#irrigOn').modal('show')

    $('#modBody').css("background-image", "url(http://192.168.1.100:1557/bw1VN7ee?container=mjpeg&stream=sub)")
    $('#startProgr').css('display', 'block');
    let imgSrc = $('#cam_pump').attr('src');
    imgSrc = imgSrc.replace("sub", "main")
    $('#modBody').css("background-image", "url(" + imgSrc + ")")
    $('#modCam').modal("show")
    valveOpen(cntr)
};


//Замыкание 2х реле
function reqRele(btnClick) {
    let url = '/btnclick/?contr=' + btnClick.slice(3, 4)  + '&rele1=' + btnClick.slice(5, 6) + '&rele2='
        + btnClick.slice(7)
    btnDisable(true, btnClick.slice(3, 4))
    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            if (response != 'Fail') {
                btnEnable(true, btnClick.slice(3, 4))
            }
            else {
                $('#mal1').text('Контроллер не доступен');
                $('#cntr4').removeClass('bg-success')
                $('#cntr4').addClass('bg-danger')
                $('#modAlert').modal('show');
            }
        }
    });
}

//Замыкание одного реле
function sinRele(contr, rele, status) {
    let url = '/singlerele/?contr=' + contr + '&rele=' + rele + '&status=' + status
    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            return(response)
        }
    })
}

//Lauran Rele
function lauRele(contr, rele, status) {
    if (contr == 5){ rele = 1} else { if (contr == 6) { rele = 2}}
    let url = '/laurele/?contr=' + contr + '&rele=' + rele + '&status=' + status // !!!!!
    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            return(response)
        }
    })
}

//Блокировка кнопок
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

//Разблокировка кнопок
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


//Чтение входов
function fooPins() {
    let contr1 = 6 // !!!!!
    let contr2 = $('#card2').text()
    readPins(contr1, 15)
    if (contr2 =! '') {
        readPins(contr2, 15)
    }
}
function readPins(contr, pin) {
    let url = '/readpin/?contr=' + contr + '&pin=' + pin
    $.ajax({
        url, url,
        type: 'GET',
        success: function (response) {
            if (response == 0) {
                $('#cntr' + contr).removeClass('bg-danger');
                $('#cntr' + contr).addClass('bg-success');
                if (on_off != 0){
                    btnEnable(true, 5)
                }
            }
            else {
                $('#cntr' + contr).removeClass('bg-success');
                $('#cntr' + contr).addClass('bg-danger');
                btnDisable(true, 5)
            }
        }
    })
}

//Минижурнал
function miniJournal() {
    let journFilter = {'first': $('#card1').text(), 'second': $('#card2').text()}
    $.ajax({
        url: '/minijourn',
        data: journFilter,
        success: function (data) {
            $('#minijourn').html(data)
        }
    })
}

//Нормы вылива
function norm(cntr, val, per=true) {
    let calc
    let values = []
    switch (cntr) {
        case '5':
            if (per == true) {
                calc = 990 / val;
                values.push(calc.toFixed(1));
            }
            else {
                calc = val * 2.03
                values.push(calc.toFixed(1));
            }
            calc = 488 / val;
            values.push(calc.toFixed(1));
            break;
        case '6':
            if (per == true) {
                calc = 1100 / val;
                values.push(calc.toFixed(1));
            }
            else {
                calc = val * 1.74
                values.push(calc.toFixed(1));
            }
            calc = 630 / val;
            values.push(calc.toFixed(1));
            break;
    }
    return values
}