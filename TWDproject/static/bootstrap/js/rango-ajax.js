$(document).ready(function() {
    // JQuery code to be added in here.
    $('#likes').click(function(){
        var catid;
        catid = $(this).attr('data-catid');
        alert(catid)
        $.get("http://192.168.1.2:8000/rango/like_category/?category_id=2", function(data){
            alert("数据：" + data + "\n状态：" + status);
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });
});