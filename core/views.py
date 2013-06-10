# Create your views here.
from django.http import HttpResponse
from lib.utils import Response
from getsocial.models import *

def login(request):
    params = {}
    return Response.render('core/users/login.html',params,request)

def register(request):
    params = {}
    return Response.render('core/users/registration.html',params,request)

def loginstep(request):
    params = {}
    if request.method == 'GET':
        if request.GET.has_key("step"):
            params['step'] = int(request.GET['step'])
    else:
        params['step'] = 1
    return Response.render('core/users/loginstep.html',params,request)