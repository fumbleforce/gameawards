from django.conf.urls import patterns, include, url

urlpatterns = patterns('gallery.views',
    url(r'add_game_pic/(?P<game_id>\d+)/$', 'add_gamepic_request'),
    url(r'del_game_pic/(?P<pic_id>\d+)/$', 'del_gamepic_request'),
    )
