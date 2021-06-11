let container = document.querySelector(".main__pics--container");

container.addEventListener("click", (e) => {
    e.preventDefault();

    const modalToggle = e.target.closest(".showDescription");

    if (!modalToggle) return;

    const modal = modalToggle.nextElementSibling;
    console.log(modal);
    const closeButton = modal.querySelector(".gallery_detail--closeButton");
    const likeButton = modal.querySelector(".likeButton");
    likeButton.addEventListener("click", () => {
        if (likeButton.classList.contains("clicked")) {
            likeButton.classList.remove("clicked");
            if (likeButton.classList.contains("heartBeat"))
                likeButton.classList.remove("heartBeat");
        } else {
            likeButton.classList.add("clicked");
            likeButton.classList.add("heartBeat");
        }
    });
    const openModal = (_) => {
        modal.classList.add("detail_show");
        modal.style.animation = "modalIn 500ms forwards";
    };
    const closeModal = (_) => {
        modal.classList.remove("detail_show");
        modal.removeEventListener("animationend", closeModal);
    };

    closeButton.addEventListener("click", () => {
        modal.style.animation = "modalOut 500ms forwards    ";
        modal.addEventListener("animationend", closeModal);
        likeButton.classList.remove("heartBeat");
    });

    openModal();
});
