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

function startInit() {
    $('#myModal').modal('show')
    $('#myModal').modal('hide')
    setTimeout(function(){
        $('#pValve1').removeClass('text-secondary');
        $('#pValve1').addClass('text-success');
    }, 2000);
    $('#pValve1').text('Задвижка открыта');

    toastInit('bg-success', 'Система запущена');
}