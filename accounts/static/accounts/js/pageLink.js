$(document).ready(function () {
    $(".page-link").onClick(function (e) {
        e.preventDefault();
        alert("hi");
        let page = $(this).attr("data-page");
        $.get("?page=" + page, function (data) {
            document.getElementById("profile_pics").innerHTML = data;
        });
    });
});
