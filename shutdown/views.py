# coding: utf-8
# shutdown/middleware.py

"""Middleware for shutdown app, downtime scheduler."""


import datetime

from django.db.models import Q
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView
from django.conf import settings

from .models import Shutdown


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


class ServiceUnavailableTemplateResponse(TemplateResponse):
    """Render a template response with status code 503 (service unavailable)."""

    status_code = 503


class ShutdownView(TemplateView):
    """Render template to display outage message to users."""

    template_name = 'shutdown/shutdown.html'
    response_class = ServiceUnavailableTemplateResponse

    def get_context_data(self, **kwargs):
        """Add some data to the regular context."""
        context = super(ShutdownView, self).get_context_data(**kwargs)

        now = datetime.datetime.now()
        shutdown_now_q = Q(start_time__lte=now) & (Q(end_time__gte=now) | Q(end_time__isnull=True))
        current_shutdowns = Shutdown.objects.filter(shutdown_now_q)

        current = None
        if current_shutdowns.count() > 0:
            candidates = [p for p in current_shutdowns if self.request.path.startswith(p.path)]
            if len(candidates):
                current = candidates[0]

        context.update({
            'contact': getattr(settings, 'SECU_FAILED_CONTACT_EMAIL', 'viphelp@austin.utexas.edu'),
            'current': current,
        })
        return context
