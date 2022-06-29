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
                    sinRele(valleyNumber, 14, 1)
                    lauRele(valleyNumber, 1, 1)
                    startInit(valleyNumber)
                }
                else {
                    reqRele('btn' + valleyNumber + '_7-9')
                    indEdit('dirInd','bg-danger', 'bg-success')
                    toastInit('bg-success', 'Система запущена без подачи воды');
                }
                if (valStatus.sis == 'True') { indEdit('sisInd','bg-danger', 'bg-success') }
                // dataSave()
                // miniJournal()
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
                lauRele(valleyNumber, 1, 0)
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
        case 'btn_p25':
            // alert(valleyNumber)
            if (on_off == 0) {
                sinRele(5, 13, 1)
                $('#btn_p25').removeClass('bg-danger')
                $('#btn_p25').addClass('bg-success')
                btnEnable(true, 5)
                on_off = 1
            }
            else {
                sinRele(5, 13, 0)
                $('#btn_p25').removeClass('bg-success')
                $('#btn_p25').addClass('bg-danger')
                btnDisable(true, 5)
                on_off = 0
            }
            break
        case 'btn5-stop':
            sinRele(5, 14, 0)
            sinRele(5, 15, 0)
            lauRele(5, 1, 0)
            break;
    }
});

//Открытие камеры
$('.img_fit').on('click', function(e) {
    let camId = e.target.id
    let imgSrc = $('#' + camId).attr('src');
    imgSrc = imgSrc.replace("sub", "main")
    // $('#full').attr('src', imgSrc)
    $('#modBody').css("background-image", "url(" + imgSrc + ")")
    $('#modCam').modal("show")
});