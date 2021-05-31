$(document).ready(function(){ 
    var page = 1;
    var empty_page = false;
    var block_request = false;
    $(window).scroll(function() {
        var margin = $(document).height() - $(window).height() - 200;
        if($(window).scrollTop() > margin && empty_page == false &&
        block_request == false) {
            block_request = true;
            page += 1;
            $.get('?page=' + page, function(data) {
                if(data == '') {
                    empty_page = true;
                }
                else {
                    block_request = false;
                    $('#image-list').append(data);
                }
            });
        }
    });
});