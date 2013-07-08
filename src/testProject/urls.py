from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from testProject import settings

urlpatterns = patterns('',
    # Admin and Accound Stuff
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    
    url(r'^accounts/', include('registration.backends.simple.urls')), 
   
    # Kniffel Links
    
    #url(r'^kniffel/$', include('kniffelApp.urls')),
    url(r'^kniffel/w/(?P<w_id>\d+)/$', 'kniffelApp.views.kniffel_w_hold', name='kniffel_w_hold'),
    #url(r'^kniffel/start/(?P<gamename>\w+)/$', 'kniffelApp.views.kniffel_start', name="kniffel_gamename"),
    url(r'^kniffel/start/$', 'kniffelApp.views.kniffel_start'),
    url(r'^kniffel/$', 'kniffelApp.views.kniffel'),
    url(r'^highscore/$', 'kniffelApp.views.highscore'),
    url(r'^download/$', 'kniffelApp.views.download'),
    url(r'^impressum/$', 'kniffelApp.views.impressum'),

    url(r'^css/bootstrap.css', 'kniffelApp.views.bootstrapcss'),
    url(r'^css/bootstrap-responsive.css', 'kniffelApp.views.bootstrapresponsivecss'),
    url(r'^js/jquery-1.10.2.js', 'kniffelApp.views.jsjquery'),

    url(r'^$', 'kniffelApp.views.home', name='home'),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
)