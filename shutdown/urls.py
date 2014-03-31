from django.conf.urls import patterns, include, url
from shutdown.views import Shutdown

urlpatterns = patterns('',
    url(r'^shutdown/$', Outage.as_view(), name='shutdown',),
)

