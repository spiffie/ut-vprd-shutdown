from django.db.models import Model, CharField


class ShutDown(Model):
    # TODO: add start and end times
    message = CharField(max_length=1000)
