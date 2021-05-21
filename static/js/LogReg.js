const regBox = document.querySelector(".registerBox");
const logBox = document.querySelector(".loginBox");
let regBut = document.querySelector(".regButton");
let logBut = document.querySelector(".logButton");
const logBoxEnter = () => {
    classClean();
    logBox.classList.add("enter");
    regBox.classList.add("exit");
};
const regBoxEnter = () => {
    classClean();
    regBox.classList.add("enter");
    logBox.classList.add("exit");
};
const classClean = () => {
    logBox.classList.remove("enter");
    logBox.classList.remove("exit");
    regBox.classList.remove("enter");
    regBox.classList.remove("exit");
};

logBut.addEventListener("click", (e) => {
    // e.preventDefault();
    logBoxEnter();
});

regBut.addEventListener("click", (e) => {
    // e.preventDefault();
    regBoxEnter();
});
