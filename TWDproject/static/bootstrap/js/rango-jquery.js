$(document).ready(function(){
    //JQuery code to be added in here.
    $("#about-btn").addClass('btn btn-primary')
    $("#about-btn").click(function(event){
        // alert("You clicked the button using JQuery!")
        msgstr = $("#msg").html()
        msgstr = msgstr + "O"
        $("#msg").html(msgstr)
    });

    $("p").hover(function(){
        $(this).css('color', 'red');
    },
    function(){
        $(this).css('color', 'black');
    });

});