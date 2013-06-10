from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^users/login/$', 'core.views.login'),
    url(r'^users/registration/$', 'core.views.register'),
    url(r'^users/loginstep/$', 'core.views.loginstep'),
)