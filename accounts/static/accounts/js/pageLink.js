$(document).ready(function () {
    $("body").on("click", ".page-link", function (e) {
        e.preventDefault();
        let page = $(this).attr("data-page");
        $.get("?page=" + page, function (data) {
            document.getElementById("profile_pics").innerHTML = data;
        });
    });
});
