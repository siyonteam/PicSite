$(document).ready(function () {
    let page = 1;
    let empty_page = false;
    let block_request = false;
    $(window).scroll(function () {
        let margin = $(document).height() - $(window).height() - 200;
        if (
            $(window).scrollTop() > margin &&
            empty_page == false &&
            block_request == false
        ) {
            block_request = true;
            page += 1;
            $.get("?page=" + page, function (data) {
                if (data == "") {
                    empty_page = true;
                } else {
                    block_request = false;
                    $("#image-list").append(data);
                }
            });
        }
    });
});
