from django.conf.urls import patterns, include, url

urlpatterns = patterns('members.views',
    url(r'^register/$', 'member_registration'),
    url(r'^login/$', 'login_request'),
    url(r'^logout/$', 'logout_request'),
    url(r'^profile/$', 'profile_request'),
    url(r'^resetpassword/$', 'reset_password_request'),
    url(r'^resetpassword/user/$', 'sent_user_request'),
    url(r'^resetpassword/email/$', 'sent_email_request'),
    url(r'^edit_member/$', 'edit_member_request'),
    
    )
