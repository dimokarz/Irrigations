$('.btn').mousedown(function(e) {
    let url = '';
    click_id=e.target.id;
    let sid_ptz = $('#pSid').text();
    let url_ptz = 'https://192.168.1.100:18082/ptz?command='
    switch(click_id) {
        case 'arr_ul':
            url_ptz = url_ptz + 'turn&speed_x=-3&speed_y=3&sid=' + sid_ptz;
            break;
        case 'arr_u':
            url_ptz = url_ptz + 'turn&speed_x=0&speed_y=3&sid=' + sid_ptz;
            break;
        case 'arr_ur':
            url_ptz = url_ptz + 'turn&speed_x=3&speed_y=3&sid=' + sid_ptz;
            break;
        case 'arr_l':
            url_ptz = url_ptz + 'turn&speed_x=-3&speed_y=0&sid=' + sid_ptz;
            break;
        case 'arr_r':
            url_ptz = url_ptz + 'turn&speed_x=3&speed_y=0&sid=' + sid_ptz;
            break;
        case 'arr_dl':
            url_ptz = url_ptz + 'turn&speed_x=-3&speed_y=-3&sid=' + sid_ptz;
            break;
        case 'arr_d':
            url_ptz = url_ptz + 'turn&speed_x=0&speed_y=-3&sid=' + sid_ptz;
            break;
        case 'arr_dr':
            url_ptz = url_ptz + 'turn&speed_x=3&speed_y=-3&sid=' + sid_ptz;
            break;
        case 'arr_zin':
            url_ptz = url_ptz + 'zoom&speed=1&sid=' + sid_ptz;
            break;
        case 'arr_zout':
            url_ptz = url_ptz + 'zoom&speed=-1&sid=' + sid_ptz;
            break;
    };
    $.ajax({
        url: url_ptz,
        type: 'POST',
        error: function(error) {
            console.log(error);
        }
    });
});

$('.btn').mouseup(function(){
    let sid_ptz = $('#sid0').text();
    url_ptz = 'https://192.168.1.100:18082/ptz?command=stop&sid=' + sid_ptz;
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