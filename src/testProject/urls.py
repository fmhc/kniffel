from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', 'kniffelApp.views.home', name='home'),
    # url(r'^testProject/', include('testProject.foo.urls')),
    url(r'^kniffel/$', 'kniffelApp.views.kniffel'),
    url(r'^highscore/$', 'kniffelApp.views.highscore'),
    url(r'^download/$', 'kniffelApp.views.download'),
    url(r'^impressum/$', 'kniffelApp.views.impressum'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^css/bootstrap.css', 'kniffelApp.views.bootstrapcss'),
    url(r'^css/bootstrap-responsive.css', 'kniffelApp.views.bootstrapresponsivecss'),
    url(r'^js/jquery-1.10.2.js', 'kniffelApp.views.jsjquery'),
    # Uncomment the next line to enable the admin:
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^accounts/', include('bootstrap_theme.registration_urls')),

    url(r'^admin/', include(admin.site.urls)),
)
