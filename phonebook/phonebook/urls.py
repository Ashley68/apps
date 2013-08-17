from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    url(r'^mainscreen/$', 'phonebookapp.views.mainscreen', name='mainscreen'),

    # Login URLs:
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

    # Password Reset URLs:
    url(r'^accounts/password_reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/accounts/password_reset/mailed/'},
        name="password_reset"),
    (r'^accounts/password_reset/mailed/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password_reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    (r'^accounts/password_reset/complete/$',
        'django.contrib.auth.views.password_reset_complete'),


    # Admin URLs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
