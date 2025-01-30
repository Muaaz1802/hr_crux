"""
hr_crux_automations/filters.py
"""

from hr_crux.filters import hr_cruxFilterSet, django_filters
from hr_crux_automations.models import MailAutomation


class AutomationFilter(hr_cruxFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
