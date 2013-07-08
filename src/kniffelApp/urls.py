'''
Created on 06.07.2013

@author: fmh
'''
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Kniffel Links
    
    url(r'^kniffel/$', include('kniffelApp.urls')),
    
    url(r'^kniffel/$', 'kniffelApp.views.kniffel'),
    #url(r'^kniffel/$', 'kniffelApp.views.kniffel'),
    url(r'^kniffel/start/(?P<gamename>\w+)/$', 'kniffelApp.views.kniffel_start', name="kniffel_gamename"),
    url(r'^kniffel/w/(?P<w_id>\d+)/$', 'kniffelApp.views.kniffel_w_hold', name='kniffel_w_hold'),
    url(r'^highscore/$', 'kniffelApp.views.highscore'),
    url(r'^download/$', 'kniffelApp.views.download'),
    url(r'^impressum/$', 'kniffelApp.views.impressum'),

    url(r'^css/bootstrap.css', 'kniffelApp.views.bootstrapcss'),
    url(r'^css/bootstrap-responsive.css', 'kniffelApp.views.bootstrapresponsivecss'),
    url(r'^js/jquery-1.10.2.js', 'kniffelApp.views.jsjquery'),

    url(r'^$', 'kniffelApp.views.home', name='home'),
)
