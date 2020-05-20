// In the name of Allah

$(function(){
    var cls = ['a','b','c','d','e','f'];
    var index = 0;
    $('div.table div.col').each(function(){
        $(this).addClass(cls[index]);
        (index == 5) ? index = 0 : index += 1;
    });
});