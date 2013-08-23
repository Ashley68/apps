from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'stuff.views.all_stuff', name="stuff"),
    url(r'^(?P<thing_id>\d+)/$',
         'stuff.views.thing_details',
          name='thing_details'),
    url(r'^create/$',
         'stuff.views.create_stuff',
          name="create_stuff"),
    url(r'^edit/(?P<thing_id>\d+)/$',
         'stuff.views.edit_stuff',
         name='edit_stuff'),
    url(r'^delete/(?P<thing_id>\d+)/$',
        'stuff.views.delete_stuff',
        name='delete_stuff'),
)