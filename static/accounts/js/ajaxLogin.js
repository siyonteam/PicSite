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

    $("body").on("click","#toggleButton",function(e){
        let action = $('#toggleButton').data("action");
        console.log(action)
        let url;
        let post_action ;
        if (action == "login"){
            url = '/accounts/register/'
            post_action = "register";
        }else{
            url = '/accounts/login/'
            post_action = "login"
        }
        $.ajax({
            url : url,
            method : 'get',
            success : function(response){
                document.getElementById("logregform").innerHTML=response;
                $('#toggleButton').attr("data-action",post_action);
                $('#toggleButton').text(action)
            }
        })
    })
});