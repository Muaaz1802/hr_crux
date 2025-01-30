"""
hr_crux_audit/settings.py

This module is used to write settings contents related to payroll app
"""

from hr_crux.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "hr_crux_audit.context_processors.history_form",
)
