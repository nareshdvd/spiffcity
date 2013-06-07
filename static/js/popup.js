$(document).ready(function()
{
    if($.browser.mozilla)
    {
        $(document).on('click', 'label', function(e)
        {
            if(e.currentTarget === this && e.target.nodeName !== 'INPUT')
            {
                $(this.control).click();
            }
        });
    }
    
    $("#add-photo-iframe").on("load",function()
    {
        success = $(this).contents().find("body").find("#add_photo_success_message").length;
        if(success == 1)
        {
            alert("photo saved successfully");
        }
        else
        {
            new_html = $(this).contents().find("body").find(".popup-container").html();   
            $(".popup-container").html(new_html);
        }
    });
});