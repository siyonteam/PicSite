let follow = document.querySelector(".profile__main--right-follow");
let isFollow = false;
let aboutPart = document.querySelector(".left__main--about");
let photosPart = document.querySelector("#profile_pics");
let aboutButton = document.getElementById("about");
let photosButton = document.getElementById("photos");

// set x-csrf token
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
    let senderId=follow.dataset.sender
    let reciverId=follow.dataset.reciver
    $.ajax({
        url : "/accounts/follow/",
        method : 'POST',
        data : {
            sender:senderId,
            reciver:reciverId
        },
        success : function(data){
            if (data.isFollow) {
                follow.textContent = "unfollow";
            } else if (!(data.isFollow)) {
                follow.textContent = "follow";
            }
            document.getElementById("followers").innerHTML=data.followers
            console.log(data.isFollow)
        }  
    });
});
