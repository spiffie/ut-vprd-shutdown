# coding: utf-8
# shutdown/models.py

"""Models for shutdown app, downtime scheduler."""


from django.db import models


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


class Shutdown(models.Model):
    """Schedule downtime for a given path."""

    path = models.CharField(max_length=1000, help_text=('Enter a full path, including leading slash, '
                                                        'but NOT a trailing slash.'))
    message = models.CharField(max_length=1000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    is_exact_match = models.BooleanField(default=False, help_text='Select to shutdown only exact path matches.')

    class Meta:
        db_table = 'REGR_SHUTDOWN'
        ordering = ('-start_time', 'path',)
        managed = True
