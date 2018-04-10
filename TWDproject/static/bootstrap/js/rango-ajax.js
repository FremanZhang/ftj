$(document).ready(function() {
    // JQuery code to be added in here.
    $('#likes').click(function(){
        var catid;
        catid = $(this).attr('data-catid');
        $.get("/rango/like_category/?category_id=2", function(data){
            alert("数据：" + data + "\n状态：" + status);
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });
});