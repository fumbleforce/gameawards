from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^(?P<event_id>\d+)/$', 'register_to_event'),
    url(r'^$', 'event_list'),
    )
