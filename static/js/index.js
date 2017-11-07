$(function() {
    // 侧边二级菜单
    $(".has_submenu > a").click(function(e) {

        var menu = $(this).parent("li");
        var sunMenu = $(this).next("ul");
 
        if (menu.hasClass("open")) {
            sunMenu.slideUp(50,function(){
                menu.removeClass("open");
            });
            
        } else {
            $(".navi > li > ul").slideUp(50);
            
            setTimeout(function(){
                $(".navi > li").removeClass("open");
                sunMenu.slideDown(50);
                menu.addClass("open");
            },50);
            
        }

        return false;
    });
});
