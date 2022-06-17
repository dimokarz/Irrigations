let valStatus = {'id': '', 'run': 'False', 'dir': '-', 'wat': 'False', 'sis': 'False',
    'valve1': 'False', 'valve2': 'False'}


$(document).ready(function() {
    let intertval1 = setInterval(foo, 2000)
    function foo() {
        readPins(1, 15)
    }
});