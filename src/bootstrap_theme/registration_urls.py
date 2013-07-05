'''from registration.views import activate, register'''
from django.conf import settings
from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView

#if 'RECAPTCHA_PUBLIC_KEY' in dir(settings):
#    from bootstrap_theme.forms import RegistrationFormCaptcha as RegistrationForm
#else:
#    from registration.forms import RegistrationForm

urlpatterns = patterns('',
    url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
)
