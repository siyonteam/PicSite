let container = document.querySelector(".main__pics--container");
let oldUrl = window.location.href;

container.addEventListener("click", (e) => {
    e.preventDefault();
    const modalToggle = e.target.closest(".showDescription");

    if (!modalToggle) return;

    const modal = modalToggle.nextElementSibling;
    var picid = modal.getAttribute("data-picid");
    var url = "/pictures/" + picid;
    $.get(url,function(data) {
        modal.innerHTML = data;
        window.history.pushState('', 'detail', url);
        
        const closeButton = modal.querySelector(".gallery_detail--closeButton");
        
        const openModal = (_) => {
            modal.classList.add("detail_show");
            modal.style.animation = "modalIn 500ms forwards";
        };
        const closeModal = (_) => {
            modal.classList.remove("detail_show");
            modal.removeEventListener("animationend", closeModal);
            window.history.pushState('', 'home', oldUrl);
            modal.innerHTML = "";
        };
        closeButton.addEventListener("click", () => {
            modal.style.animation = "modalOut 500ms forwards    ";
            modal.addEventListener("animationend", closeModal);
        
        });

        openModal();
    });
});
