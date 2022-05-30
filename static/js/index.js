$(document).ready(function() {
    for (st in st_lst) {
        let actuals = JSON.parse('{{ st_lst }}');
        alert(actuals)
    }
});