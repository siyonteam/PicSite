let regBox = document.querySelector(".registerBox");
let logBox = document.querySelector(".loginBox");
const classClean = () => {
    logBox.classList.remove("enter");
    logBox.classList.remove("exit");
    regBox.classList.remove("enter");
    regBox.classList.remove("exit");
};
logBox.addEventListener("click", (e) => {
    // e.preventDefault();
    classClean();
    logBox.classList.add("enter");
    regBox.classList.add("exit");
});
regBox.addEventListener("click", (e) => {
    // e.preventDefault();
    classClean();
    regBox.classList.add("enter");
    logBox.classList.add("exit");
});
