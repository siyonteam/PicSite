var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
let alertDiv = document.querySelector(".alert");
let alertFuncion = (alertStatus, alertStatusRemove, alertText, time) => {
    alertDiv.classList.add(alertStatus);
    alertDiv.textContent = alertText;
    alertDiv.style.display = "block";
    setTimeout(() => {
        alertDiv.style.display = "none";
        alertDiv.classList.remove(alertStatusRemove);
    }, time);
};

$(document).ready(function () {
    $("body").on("click","#regButton",function(e){
        $.ajax({
            url : '',
            method : 'post',
            data : $("#Form").serialize(),
            success : function(response){
                if(response.status == "1"){
                    window.location.href=response.url;
                }else{
                    alertFuncion(
                        "alert-danger",
                        "alert-danger",
                        response.message,
                        3000
                    );
                }
            }
        })
    })
});