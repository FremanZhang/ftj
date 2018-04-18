$(document).ready(function() {
    // JQuery code to be added in here.
    $('#likes').click(function(){
        var catid;
        catid = $(this).attr('data-catid');
        alert(catid)
        $.get("/rango/like_category/", {category_id: catid}, function(data){
            alert("数据：" + data + "\n状态：" + status);
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });

    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/rango/suggest_category/', {suggestion: query}, function(data){
            // alert(data)
            $('#cats').html(data);
        });
    });

    $('.rango-add').click(function(){
        var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this);
        $.get('/rango/auto_add_page/', {category_id: catid, url:url, title:title}, function(data){
            $('#pages').html(data);
            me.hide();
        });
    });

});