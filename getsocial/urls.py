from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'getsocial.views.index'),
    url(r'^albums/add/$', 'getsocial.views.add_album'),
    url(r'^photos/add/$', 'getsocial.views.add_photo'),
    url(r'^photos/category/(?P<category_id>[0-9]*)/$', 'getsocial.views.categoryphotos')
)
