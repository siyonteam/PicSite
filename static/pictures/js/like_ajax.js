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

function like(elmnt){
    $.post('/pictures/like/',
        {
            id : elmnt.dataset.id,
        },
        function(data){
            console.log(data.isLike)
            if (data.isLike == true) {
                elmnt.classList.add("clicked");
            } else if(data.isLike == false) {
                elmnt.classList.remove("clicked");
            }else {
                if (window.confirm('you must login for like , clik ok to login ')) 
                {
                    window.location.href=data.loginUrl;
                };
            }
        }
    ); 
} 
