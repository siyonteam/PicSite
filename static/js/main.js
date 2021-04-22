//jQuery
$(document).ready(() => {
    $(window).bind("scroll", function () {
        var navHeight = $("#header").height();
        if ($(window).scrollTop() > navHeight) {
            $("#topheader").addClass("fixed");
        } else {
            $("#topheader").removeClass("fixed");
        }
    });
    $("#showdisc").click(() => {
        $("#showdisc").fadeOut();
        $(".header__bestMonth--disc").slideDown();
    });
    $("#closedisk").click(() => {
        $("#showdisc").fadeIn();
        $(".header__bestMonth--disc").slideUp();
    });

    $(".owl-carousel").owlCarousel({
        rtl: true,
        // loop: true,
        // center: true,
    });
});

// JavaScript
const bestMonth = document.querySelector(".header__bestMonth");
const headerTag = document.querySelector(".header__tag");
const topHeaderLeft = document.querySelector(".topHeader__left");
const topHeaderRight = document.querySelector(".topHeader__right");
const category = document.querySelector(".main__categories");
const pics = document.querySelector(".main__pics");
const anim = new TimelineMax();
anim.fromTo(bestMonth, 1, { x: "-100%" }, { x: "0%", ease: Power2.easeInOut })
    .fromTo(
        bestMonth,
        1,
        { width: "50vw" },
        { width: "60vw", ease: Power2.easeInOut },
        "-=0.5"
    )
    .fromTo(
        headerTag,
        1,
        { opacity: "0" },
        { opacity: "1", ease: Power2.easeInOut },
        "-=0.5"
    )
    .fromTo(
        headerTag,
        1,
        { width: "0vw" },
        { width: "20vw", ease: Power2.easeInOut },
        "-=1.2"
    )
    .fromTo(
        topHeaderLeft,
        0.5,
        { opacity: "0" },
        { opacity: "1", ease: Power2.easeInOut },
        "-=1.5"
    )
    .fromTo(
        topHeaderRight,
        1,
        { opacity: "0" },
        { opacity: "1", ease: Power2.easeInOut },
        "-=1.8"
    )
    .fromTo(
        category,
        1,
        { opacity: "0" },
        { opacity: "1", ease: Power2.easeInOut },
        "-=1.8"
    )
    .fromTo(
        pics,
        1,
        { opacity: "0" },
        { opacity: "1", ease: Power2.easeInOut },
        "-=1.8"
    );
