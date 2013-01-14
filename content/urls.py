from django.conf.urls import patterns, include, url

urlpatterns = patterns('content.views',
    url(r'^$', 'info_request'),
    url(r'info/$', 'info_request'),
)
