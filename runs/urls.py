from django.conf.urls import patterns, include, url

urlpatterns = patterns('runs.views',
    url(r'^$', 'game_list_request'),
    url(r'^(?P<game_id>\d+)/$', 'game_request'),
    url(r'register/$', 'game_registration_request'),
    url(r'edit/(?P<game_id>\d+)/$', 'game_edit_request'),
    )
