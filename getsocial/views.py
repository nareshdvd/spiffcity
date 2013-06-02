# Create your views here.
from django.http import HttpResponse
from lib.utils import Response
from getsocial.forms import PhotoForm, AlbumForm
from getsocial.models import *
def login(request):
    params = {}
    return Response.render('getsocial/login.html',params,request)

def index(request):
    params = {}
    return Response.render('getsocial/index.html',params,request)

def add_photo(request):
    if not request.user.is_authenticated():
        return HttpResponse("not_authenticated")
    form_data_saved = False
    if request.POST:
        form = PhotoForm(request.user, request.POST,request.FILES)
        print request.FILES
        if form.is_valid() and form.is_multipart():
            cd = form.cleaned_data
            album = Album.objects.get(id = cd['album'])
            title = cd['title']
            cover_image = cd['cover_image']
            featured = cd['featured']
            city = City.objects.get(id = cd['city'])
            image = request.FILES['image']
            photo = Photo(
                title = title,
                album = album,
                image = image,
                cover_image = cover_image,
                featured = featured,
                city = city
            )
            photo.save()
            form_data_saved = True
        else:
            form_data_saved = False
    else:
        form = PhotoForm(request.user)
    
    params = {}
    if form_data_saved:
        params['success'] = True
    else:
        params['form'] = form
    
    return Response.render('getsocial/photos/add.html',params,request)

def add_album(request):
    if not request.user.is_authenticated():
        return HttpResponse("not_authenticated")
    form_data_saved = False
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            category = Category.objects.get(id = cd['category'])
            title = cd['title']
            album = Album(
                title = title,
                category = category,
                user = request.user
            )
            album.save()
            form_data_saved = True
        else:
            form_data_saved = False
    else:
        form = AlbumForm()
    params = {}
    if form_data_saved:
        params['success'] = True
    else:
        params['form'] = form
    
    return Response.render('getsocial/albums/add.html',params,request)