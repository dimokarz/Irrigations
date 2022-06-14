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
                    alert(valStatus.run + valStatus.valve1)
                    startInit()
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
            dataSave()
            indEdit('All', 'bg-success', 'bg-danger')
            toastInit('bg-success', 'Система остановлена');
            break;
        // Направление
        case 'btn' + valleyNumber + '_7-10':
            $('#dirInd' + valleyNumber).text('Вперёд');
            valStatus.dir = 'F'
            break;
        case 'btn' + valleyNumber + '_8-10':
            $('#dirInd' + valleyNumber).text('Назад');
            valStatus.dir = 'R'
            break;
        // Вода
        case 'btn' + valleyNumber + '_7-11':
            $('#watInd' + valleyNumber).text('Вкл');
            valStatus.wat = 'True'
            break;
        case 'btn' + valleyNumber + '_8-11':
            $('#watInd' + valleyNumber).text('Выкл');
            valStatus.wat = 'False'
            break;
        // Автопарковка
        case 'btn' + valleyNumber + '_7-12':
            $('#sisInd' + valleyNumber).text('Вкл');
            valStatus.sis = 'True'
            break;
        case 'btn' + valleyNumber + '_8-12':
            $('#sisInd' + valleyNumber).text('Выкл');
            valStatus.sis = 'False'
            break;
    };
    let url = '/btnclick/1'
    $.ajax({
        url: url,
        type: 'GET',
        error: function(error) {
            console.log(error);
        }
    });
});

//Открытие камеры
$('img').on('click', function(e) {
    $('#modCam1').modal("show")
});