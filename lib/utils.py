from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from spiffcity import settings
import os,sys
from PIL import Image
from getsocial.models import *

def enum(**enums):
    return type('Enum', (), enums)

class Response:
    THUMBNAIL_TYPE = enum(
        SQUARE = 'tsq',
        FIXED_HEIGHT = 'tfh',
        FIXED_WIDTH = 'tfw'
    )
    @staticmethod
    def render(template,params,request):
        params['img_url'] = settings.STATIC_IMAGE_URL
        params['js_url'] = settings.STATIC_JS_URL
        params['css_url'] = settings.STATIC_CSS_URL
        params['media_url'] = settings.MEDIA_URL
        all_categories = Category.objects.all
        params['all_categories'] = all_categories
        response = render_to_response(template,params,context_instance=RequestContext(request))
        return response

class Imaging:
    def __init__(self,image,width,height):
        self.image_name = image.path
        self.image = Image.open(self.image_name)
        self.width = width
        self.height = height
    
    def thumbnail_fixed_width(self,new_width,save_to = ""):
        temp_image = self.image.copy()
        old_size_ratio = (self.height * 1.0)/self.width
        new_height = old_size_ratio * new_width
        new_height = int(round(new_height))
        temp_image.thumbnail((new_width,new_height),Image.ANTIALIAS)
        new_image, ext = os.path.splitext(self.image_name)
        ext = str(ext.split('.')[1])
        if (ext == 'jpg') or (ext == 'JPG'):
            ext = 'jpeg'
        new_image = new_image + ".tfw." + ext
        temp_image.save(new_image,ext)
        return True
    
    def thumbnail_fixed_height(self,new_height, save_to = ""):
        temp_image = self.image.copy()
        old_size_ratio = (self.width * 1.0)/self.height
        new_width = old_size_ratio * new_height
        new_width = int(round(new_width))
        temp_image.thumbnail((new_width,new_height),Image.ANTIALIAS)
        new_image, ext = os.path.splitext(self.image_name)
        ext = str(ext.split('.')[1])
        if (ext == 'jpg') or (ext == 'JPG'):
            ext = 'jpeg'
        new_image = new_image + ".tfh." + ext
        temp_image.save(new_image,ext)
        return True
    
    def thumbnail_square(self, new_width, save_to = ""):
        temp_image = self.image.copy()
        new_height = new_width
        temp_image.thumbnail((new_width,new_height),Image.ANTIALIAS)
        new_image, ext = os.path.splitext(self.image_name)
        ext = str(ext.split('.')[1])
        if (ext == 'jpg') or (ext == 'JPG'):
            ext = 'jpeg'
        new_image = new_image + ".tsq." + ext
        temp_image.save(new_image,ext)
        return True
    
    @staticmethod
    def get_thubnail_path(self,file_path,thumb_type="tsq"):
        thumb_image_name = ''
        
        image_name, ext = os.path.splitext(file_path)
        ext = ext.split('.')[0]
        thumb_image_name = image_name + "."+thumb_type+"." + ext
        return thumb_image_name