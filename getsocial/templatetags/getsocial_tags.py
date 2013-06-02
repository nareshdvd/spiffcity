from django import template
from django.utils.safestring import mark_safe
from spiffcity import settings
register = template.Library()

@register.simple_tag
def get_image_tag(image_name,image_class="",*args,**kwargs):
    extra_params = ''
    if kwargs.has_key("height"):
        extra_params = extra_params + " height='"+kwargs['height']+"'"
    if kwargs.has_key("width"):
        extra_params = extra_params + " width='"+kwargs['width']+"'"
    
    if len(kwargs) > 0:    
        for key,val in kwargs.iteritems():
            if key != 'data':
                extra_params = extra_params + " " + key + "='" + val + "'"
    if kwargs.has_key("data"):
        data = kwargs["data"]
        arr_data_temp = data.split(";")
        for ad in arr_data_temp:
            arr_data = ad.split(":")
            extra_params = extra_params + " data-" + arr_data[0] + "='" + arr_data[1] + "'"
    image_tag = "<img src='"+settings.STATIC_IMAGE_URL+image_name+"' class='"+image_class+"' "+extra_params+"/>"
    return mark_safe(image_tag)

@register.simple_tag
def get_script_tag(script_name):
    script_tag = "<script type='text/javascript' src='" + settings.STATIC_JS_URL + "" + script_name + "'></script>"
    return script_tag