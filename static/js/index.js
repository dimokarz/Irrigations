let valStatus = {'id': '', 'run': 'False', 'dir': '-', 'wat': 'False', 'sis': 'False',
    'valve1': 'False', 'valve2': 'False'}


$(document).ready(function() {
    switch (document.location.pathname) {
        case '/login/':
            $('body').css('background-size', 'cover')
            $('body').css('background-image', 'url(/static/img/valley.jpg)')
            break
        case '/simple/':
            $('body').css('background-image', '')
            let intertval1 = setInterval(foo, 2000)
            function foo() {readPins(1, 15)}
            break
        default:
            $('body').css('background-image', '')
            break
    }
})