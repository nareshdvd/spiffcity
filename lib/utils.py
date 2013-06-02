from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from spiffcity import settings

from getsocial.models import *

class Response:
    @staticmethod
    def render(template,params,request):
        params['img_url'] = settings.STATIC_IMAGE_URL
        params['js_url'] = settings.STATIC_JS_URL
        params['css_url'] = settings.STATIC_CSS_URL
        
        all_categories = Category.objects.all
        params['all_categories'] = all_categories
        response = render_to_response(template,params,context_instance=RequestContext(request))
        return response