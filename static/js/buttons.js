// Проверка выбранных систем
function btn_sel() {
    let duet = []
    let valley = []
    let inputElems = document.getElementsByTagName("input"),
    count = 0;
    inuptId = []
    for (let i=0; i<inputElems.length; i++) {
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
            if ($('#dirInd' + valleyNumber).text() == '---') {
                toastInit('bg-danger', 'Не выбрано направление');
            };
            break;
        // Стоп
        case 'btn' + valleyNumber + '_8-9':
            toastInit('bg-success', 'Система остановлена');;
            break;
        // Направление
        case 'btn' + valleyNumber + '_7-10':
            $('#dirInd' + valleyNumber).text('Вперёд');
            break;
        case 'btn' + valleyNumber + '_8-10':
            $('#dirInd' + valleyNumber).text('Назад');
            break;
        // Вода
        case 'btn' + valleyNumber + '_7-11':
            $('#watInd' + valleyNumber).text('Вкл');
            break;
        case 'btn' + valleyNumber + '_8-11':
            $('#watInd' + valleyNumber).text('Выкл');
            break;
        // Автопарковка
        case 'btn' + valleyNumber + '_7-12':
            $('#sisInd' + valleyNumber).text('Вкл');
            break;
        case 'btn' + valleyNumber + '_8-12':
            $('#sisInd' + valleyNumber).text('Выкл');
            break;
    };
});