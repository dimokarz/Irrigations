let valStatus = {'id': '', 'run': 'False', 'dir': '-', 'wat': 'False', 'sis': 'False',
    'valve1': 'False', 'valve2': 'False', 'fail': 'False', 'perc': '', 'dep': ''}
let on_off = 0
let lauInp
let vallRun = 0
let camId = ''
let ptzUrl = ''
let currVal = 0
let currVar = {'name': '', 'value': '', 'digit': 0}
let currId = ''
let perc = true

$(document).ready(function() {
    switch (document.location.pathname) {
        case '/login/':
            $('body').css('background-size', 'cover')
            $('body').css('background-image', 'url(/static/img/valley.jpg)')
            break
        case '/simple/':

            $('body').css('background-image', '')
            // let intertval1 = setInterval(fooPins, 2000)
            // function fooPins() {readPins(5, 15)}
            vallState()
            break
        default:
            $('body').css('background-image', '')
            break
    }
})