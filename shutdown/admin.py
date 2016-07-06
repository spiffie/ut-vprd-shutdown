# coding: utf-8
# shutdown/admin.py

"""Shutdown Django admin classes."""


from __future__ import unicode_literals

from django.contrib import admin

from .models import Shutdown


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'

__all__ = (
    'ShutdownAdmin',
)


@admin.register(Shutdown)
class ShutdownAdmin(admin.ModelAdmin):
    """Schedule a shutdown event."""

    list_display = ('path', 'start_time', 'end_time',)

    def has_module_permission(self, request):
        """Determine if admin module is listed on main page."""
        return request.user.is_superuser

    def has_add_permission(self, request):
        """Determine if current user has add permission."""
        return self.has_module_permission(request)

    def has_change_permission(self, request, obj=None):
        """Determine if current user has edit permission."""
        return self.has_module_permission(request)

    def has_delete_permission(self, request, obj=None):
        """Determine if current user has delete permission."""
        return self.has_module_permission(request)
