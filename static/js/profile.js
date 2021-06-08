let follow = document.querySelector(".left__header--follow");
let isFollow = false;
follow.addEventListener("click", () => {
    console.log(`Follow : ${isFollow}`);
    if (isFollow) {
        follow.textContent = "Follow";
        isFollow = false;
    } else {
        follow.textContent = "Following";
        isFollow = true;
    }
});
