# Create your views here.
from django.http import HttpResponse
from lib.utils import Response
from getsocial.models import *

def login(request):
    params = {}
    return Response.render('core/users/login.html',params,request)