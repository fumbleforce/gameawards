from django.conf.urls import patterns, include, url
from gameawards import settings
from django.contrib import admin
admin.autodiscover()
import os, socket

if socket.gethostname() == "TheMatrix" or "Virus":
    urlpatterns = patterns('',
        url(r'^$', 'news.views.index'),
        url(r'^news/', include('news.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^runs/', include('runs.urls')),
        url(r'^members/', include('members.urls')),
        url(r'^content/', include('content.urls')),
        url(r'^info/', 'content.views.info_request'),
        url(r'^login/', 'members.views.login_request'),
        url(r'^logout/', 'members.views.logout_request'),
        url(r'^profile/', 'members.views.profile_request'),
        url(r'^games/', 'runs.views.game_list_request'),
        url(r'^gallery/', include('gallery.urls')),
    )
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
    
else:
    urlpatterns = patterns('',
        url(r'^$', 'news.views.index'),
        url(r'^news/', include('news.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^runs/', include('runs.urls')),
        url(r'^members/', include('members.urls')),
        url(r'^content/', include('content.urls')),
        url(r'^info/', 'content.views.info_request'),
        url(r'^login/', 'members.views.login_request'),
        url(r'^logout/', 'members.views.logout_request'),
        url(r'^profile/', 'members.views.profile_request'),
        url(r'^games/', 'runs.views.game_list_request'),
        url(r'^gallery/', include('gallery.urls')),
    )
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
    


