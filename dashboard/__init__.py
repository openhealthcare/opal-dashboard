"""
Declares our Dashboard discoverable feature
"""
from django.conf import settings

from opal.utils import stringport, camelcase_to_underscore

from opal.core import discoverable

class Dashboard(discoverable.DiscoverableFeature):
    module_name = 'dashboards'
    description = None
