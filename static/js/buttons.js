//Активация кнопки "Открыть"
$(".form-check-input").on("click", function() {
    $("#btn_sel").prop("disabled", false);
});


//Кнопки
$('.btn').on('click', function(e) {
    // alert(e.target.id)
    valleyNumber = e.target.id.slice(3,4)
    switch (e.target.id) {
        // Открыть панель управления
        case 'btn_sel':
            btn_sel()
            break;
        // Старт
        case 'btn' + valleyNumber + '_7-9':
            // Проверка выбора направления
            if ($('#dirInd' + valleyNumber).text() == '---') {
                $('#mal1').text("Не выбрано направление");
                $('#modAlert').modal("show");
            }
            else {
                valStatus.id = valleyNumber
                valStatus.run = 'True'
                if (valStatus.wat == 'True') {
                    valStatus.valve1 = 'True'
                    valStatus.valve2 = 'True'
                    valStatus.fail = 'True'
                    vallRun = valleyNumber
                    sinRele(valleyNumber, 14, 1)
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    if (valleyNumber == 5) {
                        lauRele(valleyNumber, 1, 1)
                    }
                    else {
                        if (valleyNumber == 6) {
                            lauRele(valleyNumber, 1, 1)
                        }
                    }
                    startInit(valleyNumber)
                }
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                else {
                    reqRele('btn' + valleyNumber + '_7-9')
                    indEdit('dirInd','bg-danger', 'bg-success')
                    toastInit('bg-success', 'Система запущена без подачи воды');
                }
                if (valStatus.sis == 'True') { indEdit('sisInd','bg-danger', 'bg-success') }
                dataSave()
                miniJournal()
                valStatus.id = valleyNumber
                valStatus.run = 'False'
                valStatus.dir = '-'
                valStatus.wat = 'False'
                valStatus.sis = 'False'
                valStatus.valve1 = 'False'
                valStatus.valve2 = 'False'
                valStatus.fail = 'False'

            }
            break;
        // Стоп
        case 'btn' + valleyNumber + '_8-9':
            $('#dirInd' + valleyNumber).text('---');
            $('#watInd' + valleyNumber).text('Выкл');
            $('#sisInd' + valleyNumber).text('Выкл');
            valStatus.id = valleyNumber
            valStatus.run = 'False'
            valStatus.dir = '-'
            valStatus.wat = 'False'
            valStatus.sis = 'False'
            valStatus.valve1 = 'False'
            valStatus.valve2 = 'False'
            reqRele(e.target.id)
            setTimeout(function () {
                sinRele(valleyNumber, 14, 0)
                sinRele(valleyNumber, 15, 0)
                if (valleyNumber == 5) {
                    lauRele(valleyNumber, 1, 0)
                }
                else {
                    if (valleyNumber == 6) {
                        lauRele(valleyNumber, 2, 0)
                    }
                }
            }, 2000);
            dataSave()
            miniJournal()
            indEdit('All', 'bg-success', 'bg-danger')
            indEdit('fail','bg-success', 'bg-danger')
             if (valStatus.wat == 'True') {
                 setTimeout(function () {
                     toastInit('bg-success', 'Система остановлена');
                 }, 90000)
             }
            break;
        // Направление
        case 'btn' + valleyNumber + '_7-10':
            $('#dirInd' + valleyNumber).text('Вперёд');
            valStatus.dir = 'F'
            reqRele(e.target.id)
            break;
        case 'btn' + valleyNumber + '_8-10':
            $('#dirInd' + valleyNumber).text('Назад');
            valStatus.dir = 'R'
            reqRele(e.target.id)
            break;
        // Вода
        case 'btn' + valleyNumber + '_7-11':
            $('#watInd' + valleyNumber).text('Вкл');
            valStatus.wat = 'True'
            reqRele(e.target.id)
            break;
        case 'btn' + valleyNumber + '_8-11':
            $('#watInd' + valleyNumber).text('Выкл');
            valStatus.wat = 'False'
            reqRele(e.target.id)
            break;
        // Автопарковка
        case 'btn' + valleyNumber + '_7-12':
            $('#sisInd' + valleyNumber).text('Вкл');
            valStatus.sis = 'True'
            reqRele(e.target.id)
            break;
        case 'btn' + valleyNumber + '_8-12':
            $('#sisInd' + valleyNumber).text('Выкл');
            valStatus.sis = 'False'
            reqRele(e.target.id)
            break;
        //Вкл\Выкл PRO2
        case 'btn' + valleyNumber + '_p2':
            if (on_off == 0) {
                sinRele(valleyNumber, 13, 1)
                $('#btn' + valleyNumber + '_p2').removeClass('bg-danger')
                $('#btn' + valleyNumber + '_p2').addClass('bg-success')
                btnEnable(true, valleyNumber)
                on_off = 1
            }
            else {
                sinRele(valleyNumber, 13, 0)
                $('#btn' + valleyNumber + '_p2').removeClass('bg-success')
                $('#btn' + valleyNumber + '_p2').addClass('bg-danger')
                btnDisable(true, valleyNumber)
                on_off = 0
            }
            break
        //Прерывание запуска
        case 'btn-stop':
            sinRele(vallRun, 14, 0)
            sinRele(vallRun, 15, 0)
            lauRele(vallRun, 2, 0)
            $('#startProgr').css('display', 'none');
            $('#modCam').modal("hide")
            toastInit('bg-success', 'Система остановлена');
            break;
        //Полная панель
        case 'btn' + valleyNumber + '_pro2':
            let currCtrl = $('#vallName' + valleyNumber).text();
            $('#currVall').text(currCtrl);
            //Добавление id кнопкам полной панели
            $('button.bfp').each(function() {
                let currId = ''
                currId = 'btn' + valleyNumber + '_';
                currId += $(this).attr('id')
                $(this).attr('id' , currId);
            });
            $('#paramEd').text('---');
            $('#fullCtrl').modal("show");
            break;
        //0-9.
        case 'btn' + valleyNumber + '_2-9':
        case 'btn' + valleyNumber + '_3-9':
        case 'btn' + valleyNumber + '_4-9':
        case 'btn' + valleyNumber + '_2-10':
        case 'btn' + valleyNumber + '_3-10':
        case 'btn' + valleyNumber + '_4-10':
        case 'btn' + valleyNumber + '_2-11':
        case 'btn' + valleyNumber + '_3-11':
        case 'btn' + valleyNumber + '_4-11':
        case 'btn' + valleyNumber + '_2-12':
        case 'btn' + valleyNumber + '_3-12':
            if (currVar.name == '') {
                $('#mal1').text('Нужно выбрать "Percent" или "Depth" ' );
                $('#modAlert').modal("show");
            }
            else {
                let tStr = $('#paramEd').text();
                tStr += $('#' + e.target.id).text()
                $('#paramEd').text(tStr);
                currVar.value += $('#' + e.target.id).text()
                currVar.digit += 1
                reqRele(e.target.id)
            }
            break;
        //Percent
        case 'btn' + valleyNumber + '_6-9':
            currVar.name = 'Percent: ';
            currVar.value = '';
            currVar.digit = 0;
            $('#paramEd').text('Enter Percent: ');
            reqRele(e.target.id)
            break;
        //Depth
        case 'btn' + valleyNumber + '_6-10':
            currVar.name = 'Depth: ';
            currVar.value = '';
            currVar.digit = 0;
            $('#paramEd').text('Enter Depth: ');
            reqRele(e.target.id)
            break;
        //Esc
        case 'btn' + valleyNumber + '_5-12':
            currVar.name = '';
            currVar.value = '';
            currVar.digit = 0;
            $('#paramEd').text('');
            reqRele(e.target.id)
            break;
        //Enter
        case 'btn' + valleyNumber + '_6-12':
            if (currVar.name == 'Percent: ' && currVar.value != '') {
                $('#percEd').text(currVar.name + currVar.value + '%');
                $('#depEd').text('Depth: ' + norm(valleyNumber, currVar.value) + 'mm')
            }
            // else {
            //     $('#mal1').text('Введите значение' );
            //     $('#modAlert').modal("show");
            // };

            if (currVar.name == 'Depth: ' && currVar.value != '') {
                $('#depEd').text(currVar.name + currVar.value + 'mm');
                $('#percEd').text('Percent: ' + norm(valleyNumber, currVar.value) + '%');
            }
            // else {
            //     $('#mal1').text('Введите значение' );
            //     $('#modAlert').modal("show");
            // };
            reqRele(e.target.id)
            currVar.name = '';
            currVar.value = '';
            currVar.digit = 0;
            $('#paramEd').text('');
            break;
        //BackSpace
        case 'btn' + valleyNumber + '_4-12':
            if (currVar.value != '') {
                let delStr = $('#paramEd').text().slice(0, -1)
                currVar.value = delStr
                $('#paramEd').text(delStr)
                reqRele(e.target.id)
            }
    }
});

//Открытие камеры
$('.img_fit').on('click', function(e) {
    let camId = e.target.id
    let imgSrc = $('#' + camId).attr('src');
    ptzUrl = $('#ptz1').text()
    imgSrc = imgSrc.replace("sub", "main")
    // $('#full').attr('src', imgSrc)
    $('#modBody').css("background-image", "url(" + imgSrc + ")")
    $('#startProgr').css('display', 'none');
    $('#modCam').modal("show")
});