from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login', 'getsocial.views.login'),
    url(r'^$', 'getsocial.views.index'),
    url(r'^albums/add/$', 'getsocial.views.add_album'),
    url(r'^photos/add/$', 'getsocial.views.add_photo')
)
