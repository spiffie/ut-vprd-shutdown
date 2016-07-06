# coding: utf-8
# shutdown/urls.py

"""Urls definitions for shutdown app."""


from django.conf.urls import url

from .views import ShutdownView


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


urlpatterns = [
    # Hook this in to your URL structure somehwere if you want to view a rendered template.
    url(r'^$', ShutdownView.as_view(), name='shutdown_test'),
]
