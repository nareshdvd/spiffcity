$(document).ready(function()
{
    $(".user-box").click(function()
    {
        if($(".user-actions").css("height") != "140px")
        {
            show_useractions();
        }
        else
        {
            hide_useractions();
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
    
    //$("#add_box-opener").live("click",function()
    //{
    //    hide_useractions();
    //    $.ajax(
    //    {
    //        url     : "/getsocial/photos/add/",
    //        type    : "get",
    //        success : function(retdata)
    //        {
    //            //$("#overlay").show();
    //            //$("#spiff-popup").html(retdata);
    //            //$("#spiff-popup").css("left",(($(window).width - $("#spiff-popup").offsetWidth())/2))
    //            $('.modal').html(retdata);
    //        }
    //    });
    //})
    //
    //$(".login-btn").live("click",function()
    //{
    //    $.ajax(
    //    {
    //        url     : "/core/users/login",
    //        type    : "get",
    //        success : function(retdata)
    //        {
    //            //$("#overlay").show();
    //            //$("#spiff-popup").append(retdata);
    //            //$("#spiff-popup").css("padding-left",(($(window).width - $("#spiff-popup").find(".login-popup").width())/2))
    //            $('.modal').html(retdata);
    //        }
    //    });
    //});
    
    $(".login-btn").click(function()
    {
        modal_options = {
            backdrop:true,
            keyboard:true,
            remote:"/core/users/login"
        }
        $(".modal").addClass("login_popup_box");
        $(".modal").modal(modal_options).width($(".modal-body").width());
        
    });
    
    
    $(".show_small_login").live("click",function()
    {
        $(".small_login_form").toggle();
    });
    $("#overlay").live("click",function()
    {
        $("#spiff-popup").html("");
        $("#overlay").hide();
    });
    
    function call_wookmark()
    {
        var options = {
            autoResize: true, // This will auto-update the layout when the browser window is resized.
            container: $('.content-inner'), // Optional, used for some extra CSS styling
            offset: 10, // Optional, the distance between grid items
            itemWidth: 230, // Optional, the width of a grid item
            align:"left"
          };
        
        var handler = $('#tiles li');
        handler.wookmark(options);
    }
    
    //imagesLoadedObj = new imagesLoaded( );
    //imagesLoadedObj.on("always",call_wookmark);
    imagesLoaded( "#tiles li", call_wookmark )
    
});

function show_useractions()
{
    $(".user-actions").animate({height:"140px"},100,function()
    {
        $(".user-actions").show();
    });
}

function hide_useractions()
{
    $(".user-actions").animate({height:"0px"},100,function()
    {
        $(".user-actions").hide();
    });
}














$(document).ready(function()
{
    
    window_width = $(window).width();
    if(window_width<900)
    {
        apply_theme_1();
    }
    else
    {
        apply_theme_2();
    }
    
    $(".menu > a").bind("mouseover",function()
    {
       curr_menu_img = $(this).find("img")
       hoversrc = $(this).find("img").data("hoversrc");
       curr_menu_img.data("onsrc",curr_menu_img.attr("src"));
       curr_menu_img.attr("src",hoversrc);
       
    });
    $(".menu > a").bind("mouseleave",function()
    {
       curr_menu_img = $(this).find("img")
       onsrc = $(this).find("img").data("onsrc");
       curr_menu_img.attr("src",onsrc);
    });
});

function apply_theme_1()
{
    unbind_theme1_events();
    unbind_theme2_events();
    $(".header-middle").hide();
    $(".menudrop-btn").bind("click.theme_1",function()
    {
        if($(".header-middle").css("display") === "block")
        {
            //console.log($(".header-middle").css("display") + "1");
            $(".header-middle").hide();
        }
        else
        {
            //console.log($(".header-middle").css("display") + "2");
            $(".header-middle").show();
        }
    });
    
    $(".menu").each(function(index)
    {
        child_id = $(this).data("child");
        child_element = $("#" + child_id);
        child_clone = child_element.clone();
        $(this).after(child_clone);
        child_element.remove();
    });
    
    
    
    $(".menu").bind("click.theme_1",function()
    {
        var currentmenu = $(this);
        var submenu = $("#"+$(this).data("child"));
        var allmenus = $(".menu");
        $.each(allmenus,function(key,menu)
        {
            if($(menu).attr("id") != currentmenu.attr("id"))
            {
                submenu_temp = $("#"+$(menu).data("child"));
                submenu_temp.hide();
            }
        });
        if(submenu.css("display") === "none")
        {
            submenu.show(100);
        }
        else
        {
            submenu.hide();
        }
    });
}

function apply_theme_2()
{
    $(".header-middle").show();
    unbind_theme1_events();
    unbind_theme2_events();
    $(".menu").each(function(index)
    {
        child_id = $(this).data("child");
        child_element = $("#" + child_id);
        child_element.clone().appendTo($(this));
        child_element.remove();
    });
    
    $(".menu").bind("mouseover.theme_2",function()
    {
        var currentmenu = $(this);
        var submenu = $("#"+$(this).data("child"));
        submenu.show();
    });
    $(".menu").bind("mouseleave.theme_2",function()
    {
        var currentmenu = $(this);
        var submenu = $("#"+$(this).data("child"));
        submenu.hide();
    });
}

$(window).resize(function()
{
    window_width = $(window).width();
    
    if(window_width<950)
    {
        apply_theme_1();
    }
    else
    {
        apply_theme_2();
    }
});

function unbind_theme1_events()
{
    $(".menu").unbind("click.theme_1");
    $(".menudrop-btn").unbind("click.theme_1");
}


function unbind_theme2_events()
{
    $(".menu").unbind("mouseover.theme_2");
    $(".menu").unbind("mouseleave.theme_2");
}








