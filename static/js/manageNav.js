let manageNav = document.querySelector(".manageNav");
let manageNavToggle = document.querySelector(".manageNav__toggle");
let svg = manageNavToggle.childNodes[1];
manageNavToggle.addEventListener("click", (e) => {
    e.preventDefault();
    manageNav.classList.toggle("clicked");
    if (manageNavToggle.childNodes[1].classList.contains("fa-chevron-left")) {
        manageNavToggle.childNodes[1].classList.add("fa-chevron-right");
        manageNavToggle.childNodes[1].classList.remove("fa-chevron-left");
    } else {
        manageNavToggle.childNodes[1].classList.add("fa-chevron-left");
        manageNavToggle.childNodes[1].classList.remove("fa-chevron-right ");
    }
});
