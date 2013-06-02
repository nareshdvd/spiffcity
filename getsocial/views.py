# Create your views here.
from django.http import HttpResponse
from lib.utils import Response
from getsocial.forms import PhotoForm, AlbumForm
def login(request):
    params = {}
    return Response.render('getsocial/login.html',params,request)

def index(request):
    params = {}
    return Response.render('getsocial/index.html',params,request)

def add_photo(request):
    if not request.user.is_authenticated():
        return HttpResponse("not_authenticated")
    
    if request.method == 'POST':
        form = request.POST.get("form")
    params = {}
    form = PhotoForm(request.user)
    params['form'] = form
    return Response.render('getsocial/photos/add.html',params,request)

def add_album(request):
    if not request.user.is_authenticated():
        return HttpResponse("not_authenticated")
    
    if request.method == 'POST':
        form = request.POST.get("form")
    params = {}
    form = AlbumForm()
    params['form'] = form
    return Response.render('getsocial/albums/add.html',params,request)