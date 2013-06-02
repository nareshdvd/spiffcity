$(document).ready(function()
{
    $(".menu").live("mouseover",function(e)
    {
        e.stopPropagation();
        $(this).find("img").attr("src","/static/img/menu"+$(this).find("img").data("id")+"_hover.png");
        $(this).find(".submenu").slideDown(200);
    });
    $(".menu").live("mouseleave",function(e)
    {
        e.stopPropagation();
        $(this).find("img").attr("src","/static/img/menu"+$(this).find("img").data("id")+"_on.png");
        $(this).find(".submenu").slideUp(200);
    });
    
    $(".user-box").click(function()
    {
        if($(".user-actions").css("height") != "140px")
        {
            $(".user-actions").animate({height:"140px"},100,function()
            {
                $(".user-actions").show();
            });
        }
        else
        {
            $(".user-actions").animate({height:"0px"},100,function()
            {
                $(".user-actions").hide();
            });
        }
    });
    
    $(".user-actions > div > span img").mouseover(function()
    {
        $(this).attr("src","/static/img/"+$(this).data("image_hover_name"));
        $(this).parent().parent().find("span").css({"color":"#E8761E"});
    });
    $(".user-actions > div > span img").mouseout(function()
    {
        $(this).attr("src","/static/img/"+$(this).data("image_name"));
        $(this).parent().parent().find("span").css({"color":"#ffffff"})
    });
    
    
    $(".user-actions  div").mouseover(function()
    {
        $(this).find("span:first img").attr("src","/static/img/"+$(this).find("span:first img").data("image_hover_name"));
        $(this).find("span:last").css({"color":"#E8761E"});
    });
    
    $(".user-actions  div").mouseout(function()
    {
        $(this).find("span:first img").attr("src","/static/img/"+$(this).find("span:first img").data("image_name"));
        $(this).find("span:last").css({"color":"#ffffff"});
    });
    
});