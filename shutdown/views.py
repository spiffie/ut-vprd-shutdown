from django.conf import settings
from django.views.generic.base import TemplateView

from shutdown.models import ShutDown

try:
    module_path, ctx_class = settings.SHUTDOWN_CONTEXT.rsplit('.',1)
    module = __import__(module_path, fromlist=[ctx_class])
    context = getattr(module, ctx_class)
except AttributeError:
    raise ImproperlyConfigured(
        'You must supply a path your own context object by setting a '
        'SHUTDOWN_CONTEXT in your settings.py file.'
    )

class ShutdownView(TemplateView):
    template_name = 'shutdown/shutdown.html'

    def get_context_data(self, **kwargs):
        ctx = super(ShutdownView, self).get_context_data(**kwargs)
        objects = ShutDown.objects.all()
        msg = objects[0].message
        ctx.update({
            'msg':msg,
            })
        return context(
            self.request,
            ctx,
            title='Service Outage',
            page_title='Service Outage',
            window_title='Service Outage',
            )

