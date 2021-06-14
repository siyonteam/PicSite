let follow = document.querySelector(".profile__main--right-follow");
let isFollow = false;
let aboutPart = document.querySelector(".left__main--about");
let photosPart = document.querySelector(".left__main--photos");
let aboutButton = document.getElementById("about");
let photosButton = document.getElementById("photos");

let photoButStyle = () => {
    aboutButton.style.color = "#757575";
    aboutButton.style.fontWeight = "normal";
    photosButton.style.color = "#424242";
    photosButton.style.fontWeight = "bold";
};
let aboutButStyle = () => {
    photosButton.style.color = "#757575";
    photosButton.style.fontWeight = "normal";
    aboutButton.style.color = "#424242";
    aboutButton.style.fontWeight = "bold";
};
aboutButton.addEventListener("click", () => {
    photosPart.style.display = "none";
    aboutPart.style.display = "flex";
    aboutButStyle();
});
photosButton.addEventListener("click", () => {
    photosPart.style.display = "flex";
    aboutPart.style.display = "none";
    photoButStyle();
});
follow.addEventListener("click", () => {
    if (isFollow) {
        follow.textContent = "Follow";
        isFollow = false;
    } else {
        follow.textContent = "Following";
        isFollow = true;
    }
});
