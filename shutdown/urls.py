from django.conf.urls import patterns, include, url
from shutdown.views import Shutdown

urlpatterns = patterns('',
    url(r'^shutdown/$', Shutdown.as_view(), name='shutdown',),
)

