from django.conf.urls import patterns, include, url

urlpatterns = patterns('runs.views',
    url(r'^$', 'games'),
    url(r'register/$', 'game_registration_request'),
    url(r'upload/$', 'submit_game_request'),
    url(r'edit/(?P<game_id>\d+)/$', 'game_edit_request'),
    url(r'add_game_dev/(?P<game_id>\d+)/$', 'add_game_dev_request'),
    url(r'game/(?P<game_id>\d+)/$', 'game'),
    url(r'(?P<year>\d+)/$', 'game_list')
)
