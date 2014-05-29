from django.conf import settings
from django.views.generic.base import TemplateView

from utdirect.templates import UTDirectContext, UTDirectTemplateAPIError

from shutdown.models import ShutDown

try:
    module_path, ctx_class = settings.SHUTDOWN_CONTEXT.rsplit('.',1)
    module = __import__(module_path, fromlist=[ctx_class])
    context = getattr(module, ctx_class)
except AttributeError:
    context = UTDirectContext


class Shutdown(TemplateView):
    template_name = 'shutdown/shutdown.html'

    def get_context_data(self, **kwargs):
        ctx = super(Shutdown, self).get_context_data(**kwargs)
        objects = ShutDown.objects.all()
        msg = objects[0].message
        ctx.update({'msg':msg, 'title':'Service Outage'})
        try:
            new_context = context(self.request, ctx)
        except UTDirectTemplateAPIError:
            try:
                api_key = settings.API_KEY
            except AttributeError:
                raise ImproperlyConfigured(
                    'If you do not supply your own context object by setting '
                    'a SHUTDOWN_CONTEXT in settings.py, then you must supply '
                    'an API_KEY in your settings, which will be used to call '
                    'the default UTDirectContext.'
                )

            new_context = context(
                self.request,
                dict=ctx,
                api_key=api_key,
                page_title='Service Outage',
                window_title='Service Outage',
            )
        return new_context

