from django.conf.urls import patterns, include, url
from gameawards import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.index'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^runs/', include('runs.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^content/', include('content.urls')),
    url(r'^info/', 'content.views.info_request'),
=======
    #url(r'^runs/', include('runs.urls')),
    #url(r'^members/', include('members.urls')),
    #url(r'^events/', include('events.urls')),
>>>>>>> 381b75204a6bf07380b4f7b4d8751169eeac119c
)

