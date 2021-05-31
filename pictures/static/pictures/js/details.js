let container = document.querySelector(".main__pics--container");
// let showDetail = document.querySelector(".imgDescription");

container.addEventListener("click", (e) => {
    e.preventDefault();
    const modalToggle = e.target.closest(".showDescription");

    if (!modalToggle) return;

    const modal = modalToggle.nextElementSibling;
    var picid = modal.getAttribute('data-picid');
    $.get('/pictures/'+picid , function(data) {
        modal.innerHTML = data
        const closeButton = modal.querySelector(".gallery_detail--closeButton");
        
        const openModal = (_) => {
            
            modal.classList.add("detail_show");
            modal.style.animation = "modalIn 500ms forwards";
        };
        const closeModal = (_) => {
            modal.classList.remove("detail_show");
            modal.removeEventListener("animationend", closeModal);
            modal.innerHTML = "";
        };
        closeButton.addEventListener("click", () => {
            modal.style.animation = "modalOut 500ms forwards    ";
            modal.addEventListener("animationend", closeModal);
        });

        openModal(); 
        console.log("ok")
    });
})
