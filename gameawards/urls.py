from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.index'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^runs/', include('runs.urls')),
    url(r'^register/$', 'runs.views.member_registration'),
    url(r'^login/$', 'runs.views.login_request'),
    url(r'^logout/$', 'runs.views.logout_request'),
    url(r'^profile/$', 'runs.views.profile_request'),
    
)

