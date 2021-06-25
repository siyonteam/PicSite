let toggleButton = document.querySelector("#toggleButton");
let loginForm = document.querySelector("#loginForm");
let registerForm = document.querySelector("#registerForm");
let formStatus = document.querySelector("#formStatus");
let checkStatus = true; // true == login
let alertDiv = document.querySelector(".alert");
let logButton = document.querySelector("#logButton");
let regButton = document.querySelector("#regButton");
let loginInputs = loginForm.childNodes;
let registerInputs = registerForm.childNodes;

let checkBox = document.querySelectorAll(".checkbox");
let formFunc = (lForm, rForm, buttonContent, fStatus) => {
    loginForm.style.display = lForm;
    registerForm.style.display = rForm;
    toggleButton.textContent = buttonContent;
    formStatus.textContent = fStatus;
};
let clearInputs = () => {
    if (checkStatus) {
        for (let i = 1; i < loginInputs.length; i += 2) {
            loginInputs[i].value = "";
        }
        checkBox[0].checked = false;
    } else {
        for (let i = 1; i < registerInputs.length; i += 2) {
            registerInputs[i].value = "";
        }
        checkBox[1].checked = false;
    }
};
let alertFuncion = (alertStatus, alertStatusRemove, alertText, time) => {
    alertDiv.classList.add(alertStatus);
    alertDiv.textContent = alertText;
    alertDiv.style.display = "block";
    setInterval(() => {
        alertDiv.style.display = "none";
        alertDiv.classList.remove(alertStatusRemove);
    }, 3000);
};
toggleButton.addEventListener("click", (e) => {
    if (checkStatus) {
        alertDiv.style.display = "none";
        formFunc("none", "flex", "Login", "ایجاد حساب کاربری");
        clearInputs();
        checkStatus = false; // false == register
    } else {
        alertDiv.style.display = "none";
        formFunc("flex", "none", "Register", "ورود به حساب کاربری");
        clearInputs();
        checkStatus = true;
    }
});

logButton.addEventListener("click", (e) => {
    if (loginInputs[1].value == "" || loginInputs[3].value == "") {
        e.preventDefault();
        alertFuncion(
            "alert-danger",
            "alert-danger",
            "نام کاربری یا رمز عبور خالی است!",
            3000
        );
    }
});
console.log(registerInputs);
regButton.addEventListener("click", (e) => {
    if (checkBox[1].checked) {
        if (
            registerInputs[1].value == "" ||
            registerInputs[3].value == "" ||
            registerInputs[5].value == "" ||
            registerInputs[7].value == ""
        ) {
            e.preventDefault();
            alertFuncion(
                "alert-danger",
                "alert-danger",
                "لطفا فیلد های خالی را پر کنید.",
                3000
            );
        } else {
            alertFuncion(
                "alert-success",
                "alert-danger",
                "حساب کاربری با موفقیت ایجاد شد.",
                3000
            );
        }
    } else {
        alertFuncion(
            "alert-danger",
            "alert-danger",
            "برای تکمیل ثبت نام نیاز به تایید قوانین دارید.",
            5000
        );
    }
});
