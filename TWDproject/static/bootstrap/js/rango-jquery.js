$(document).ready(function(){
    //JQuery code to be added in here.
    $("#about-btn").click(function(event){
        alert("You clicked the button using JQuery!")
    });

    $("p").hover(function(){
        $(p).css('color', 'red');
    },
    function(){
        $(p).css('color', 'black');
    });

});