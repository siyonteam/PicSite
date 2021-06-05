
function like(elmnt){
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
    $.post('/pictures/like/',
        {
            id : elmnt.dataset.id,
        },
        function(data){
            if (data == "liked") {
                elmnt.style.color = "red";
            } else if(data == "unliked") {
                elmnt.style.color = "black";
            }
        }
    ); 
} 
