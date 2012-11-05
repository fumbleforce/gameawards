from django.conf.urls import patterns, include, url
from gameawards import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.index'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^games/', include('runs.urls')),
    url(r'^members/', include('members.urls')),
    
)

