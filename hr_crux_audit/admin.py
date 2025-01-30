"""
admin.py
"""

from django.contrib import admin

from hr_crux_audit.models import AuditTag, hr_cruxAuditInfo, hr_cruxAuditLog

# Register your models here.

admin.site.register(AuditTag)
