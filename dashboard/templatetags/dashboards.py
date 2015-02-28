"""
Dashboard template tags
"""
from django import template

register = template.Library()

@register.inclusion_tag('dashboard/widget.html')
def dashboard_widget(widget):
    return dict(widget=widget)
