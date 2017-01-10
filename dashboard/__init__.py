"""
Declares our Dashboard discoverable feature
"""
from django.conf import settings

from opal.utils import stringport, camelcase_to_underscore

from opal.core import discoverable
from dashboard import plugin # Don't do this once we've updated plugins in Opal

class Dashboard(discoverable.DiscoverableFeature):
    module_name = 'dashboards'
    description = None
