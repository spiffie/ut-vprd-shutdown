from django.conf import settings
from django.conf.urls import patterns, include, url
from shutdown.views import Shutdown

try:
    shutdown_url = settings.SHUTDOWN_URL
except AttributeError:
    shutdown_url = r'^shutdown/$'

urlpatterns = patterns('',
    url(shutdown_url , Shutdown.as_view(), name='shutdown',),
)

