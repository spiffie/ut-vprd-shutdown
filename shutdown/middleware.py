# coding: utf-8
# shutdown/middleware.py

"""Middleware for shutdown app, downtime scheduler."""


import datetime
import sys

from django.db.models import Q
from django.conf import settings

from .models import Shutdown
from .views import ShutdownView


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


_using_manage = True in ['manage.py' in arg for arg in sys.argv]

TESTING = ((_using_manage and 'test' in sys.argv) or ('nosetests' in sys.argv))


class ShutdownMiddleware(object):
    """Check if current request path is currently shutdown."""

    def process_request(self, request):
        """Grab path from current request."""
        if settings.STATIC_URL in request.path:
            return None

        # Django tests may set their own ROOT_URLCONF, in which case we may not
        # be able to resolve 'shutdown', so we'll just return None unless
        # testing this app intentionally.
        if TESTING and set(['shutdown', 'test_shutdown']).isdisjoint(sys.argv):
            return None

        now = datetime.datetime.now()
        shutdown_now_q = Q(start_time__lte=now) & (Q(end_time__gte=now) | Q(end_time__isnull=True))
        split_path = request.path.split('/')
        candidates = ['/'.join(split_path[:x]) for x in xrange(1, len(split_path)) if '/'.join(split_path[:x])]
        shutdown_path_q = Q()
        for cand in candidates:
            shutdown_path_q = shutdown_path_q | Q(path=cand)
        shutdown_path_q = shutdown_path_q & Q(is_exact_match=False) | Q(path=request.path) & Q(is_exact_match=True)

        current_shutdowns = Shutdown.objects.filter(shutdown_now_q & shutdown_path_q)

        if current_shutdowns.count() > 0:
            return ShutdownView.as_view()(request)

        return None
