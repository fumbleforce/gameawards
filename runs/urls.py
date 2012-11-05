from django.conf.urls import patterns, include, url

urlpatterns = patterns('runs.views',
    url(r'^$', 'game_list_request'),
    url(r'^(?P<game_id>\d+)/$', 'game_request'),
    )
