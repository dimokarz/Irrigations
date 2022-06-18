let valStatus = {'id': '', 'run': 'False', 'dir': '-', 'wat': 'False', 'sis': 'False',
    'valve1': 'False', 'valve2': 'False'}


$(document).ready(function() {
    if (document.location.href.replace(/(.+\w\/)(.+)/,"/$2") == '/?next=/') {
        $('body').css('background-size', 'cover')
        $('body').css('background-image', 'url(/static/img/valley.jpg)');
    }
    else {
        $('body').css('background-image', '');
        // let intertval1 = setInterval(foo, 2000)
        // function foo() {
        //     readPins(1, 15)
        // }
    }
});