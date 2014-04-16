import sys

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from shutdown.models import ShutDown

_using_manage = True in ['manage.py' in arg for arg in sys.argv]

TESTING = ((_using_manage and 'test' in sys.argv) or ('nosetests' in sys.argv))


class ShutdownMiddleware(object):
    def process_request(self, request):

        # Django tests may set their own ROOT_URLCONF, in which case we may not
        # be able to resolve 'shutdown', so we'll just return None unless
        # testing this app intentionally.
        if TESTING and 'shutdown' not in sys.argv:
            return None

        if (request.path == reverse('shutdown') or
            settings.STATIC_URL in request.path
            ):
            return None

        if ShutDown.objects.count() == 1:
            return redirect('shutdown')

        return None
