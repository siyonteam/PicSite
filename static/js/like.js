const likeClicked = (e) => {
    e.target.closest(".likeButton").classList.toggle("clicked");
    e.target.closest(".likeButton").classList.toggle("heartBeat");
};
