//Активация кнопки "Открыть"
$(".form-check-input").on("click", function() {
    $("#btn_sel").prop("disabled", false);
});


//Кнопки
$('.btn').on('click', function(e) {
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
                    // startInit(valleyNumber)
                    sinRele(valleyNumber, 14, 1)
                    lauRele(valleyNumber, 1, 1)
                    startInit(valleyNumber)

                }
                else {
                    indEdit('dirInd','bg-danger', 'bg-success')
                    toastInit('bg-success', 'Система запущена без подачи воды');
                }
                if (valStatus.sis == 'True') { indEdit('sisInd','bg-danger', 'bg-success') }
                dataSave()
                valStatus.id = valleyNumber
                valStatus.run = 'False'
                valStatus.dir = '-'
                valStatus.wat = 'False'
                valStatus.sis = 'False'
                valStatus.valve1 = 'False'
                valStatus.valve2 = 'False'
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
                lauRele(valleyNumber, 1, 0)
            }, 2000);
            dataSave()
            indEdit('All', 'bg-success', 'bg-danger')
            toastInit('bg-success', 'Система остановлена');
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
    }
});

//Открытие камеры
$('img').on('click', function(e) {
    $('#modCam1').modal("show")
});