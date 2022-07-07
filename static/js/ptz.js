// https://192.168.1.220:18083/ptz?command=open&channel=hNbJnraI&sid=LXq049D0
$('.btn').mousedown(function(e) {
    let url = '';
    click_id=e.target.id;
    switch(click_id) {
        case 'arr_ul':
            ptzUrl = ptzUrl.replace('XXX', '-3')
            ptzUrl = ptzUrl.replace('YYY', '3')
            break;
        case 'arr_u':
            ptzUrl = ptzUrl.replace('XXX', '0')
            ptzUrl = ptzUrl.replace('YYY', '3')
            alert(ptzUrl)
            break;
        case 'arr_ur':
            ptzUrl = ptzUrl.replace('XXX', '3')
            ptzUrl = ptzUrl.replace('YYY', '3')
            break;
        case 'arr_l':
            ptzUrl = ptzUrl.replace('XXX', '-3')
            ptzUrl = ptzUrl.replace('YYY', '0')
            break;
        case 'arr_r':
            ptzUrl = ptzUrl.replace('XXX', '3')
            ptzUrl = ptzUrl.replace('YYY', '0')
            break;
        case 'arr_dl':
            ptzUrl = ptzUrl.replace('XXX', '-3')
            ptzUrl = ptzUrl.replace('YYY', '-3')
            break;
        case 'arr_d':
            ptzUrl = ptzUrl.replace('XXX', '0')
            ptzUrl = ptzUrl.replace('YYY', '-3')
            break;
        case 'arr_dr':
            ptzUrl = ptzUrl.replace('XXX', '3')
            ptzUrl = ptzUrl.replace('YYY', '-3')
            break;
        // case 'arr_zin':
        //     url_ptz = url_ptz + 'zoom&speed=1&sid=' + sid_ptz;
        //     break;
        // case 'arr_zout':
        //     url_ptz = url_ptz + 'zoom&speed=-1&sid=' + sid_ptz;
        //     break;
    };
    $.ajax({
        url: ptzUrl,
        type: 'POST',
        error: function(error) {
            console.log(error);
        }
    });
});

$('.btn').mouseup(function(){
    // let sid_ptz = $('#sid0').text();
    url_ptz = 'https://192.168.1.220:18083/ptz?command=' + sid_ptz;
    switch(click_id) {
        case 'arr_ul':
        case 'arr_u':
        case 'arr_ur':
        case 'arr_l':
        case 'arr_fp':
        case 'arr_r':
        case 'arr_dl':
        case 'arr_d':
        case 'arr_dr':
        case 'arr_zin':
        case 'arr_zout':
            $.ajax({
                url: url_ptz,
                type: 'POST',
                error: function(error) {
                    console.log(error);
                }
            });
            break;
    }
});