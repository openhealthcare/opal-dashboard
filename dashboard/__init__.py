"""
Plugin definition for the dashboard OPAL plugin
"""
from django.conf import settings

from opal.core.plugins import OpalPlugin
from opal.utils import stringport, camelcase_to_underscore

import dashboard.widgets as widgets
from dashboard.urls import urlpatterns

# So we only do it once
IMPORTED_FROM_APPS = False

def import_from_apps():
    """
    Iterate through installed apps attempting to import app.wardrounds
    This way we allow our implementation, or plugins, to define their
    own ward rounds. 
    """
    print "Importing from apps"
    for app in settings.INSTALLED_APPS:
        try:
            stringport(app + '.dashboards')
        except ImportError:
            pass # not a problem
    global IMPORTED_FROM_APPS
    IMPORTED_FROM_APPS = True
    return

class DashboardPlugin(OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.dashboard': [
            'js/dashboard/app.js',
            # 'js/dashboard/controllers/larry.js',
            # 'js/dashboard/services/larry.js',
        ]
    }
    menuitems = [
        dict(
            href='/dashboards/', display="Dashboards", icon="fa fa-dashboard",
            activepattern='/dashboards'
        )
    ]

    def restricted_teams(self, user):
        """
        Return any restricted teams for particualr users that our
        plugin may define.
        """
        return []

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def flows(self):
        """
        Return any custom flows that our plugin may define
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}


class Dashboard(object):
    """
    Base Dashboard class.
    """
    name        = None
    description = None
    
    @classmethod
    def get(klass, name):
        """
        Return a specific ward round by slug
        """
        if not IMPORTED_FROM_APPS:
            import_from_apps()
            
        for sub in klass.__subclasses__():
            if sub.slug() == name:
                return sub
            
    @classmethod
    def list(klass):
        """
        Return a list of all ward rounds
        """
        if not IMPORTED_FROM_APPS:
            import_from_apps()
        print klass.__subclasses__()
        return klass.__subclasses__()

    @classmethod
    def slug(klass):
        return camelcase_to_underscore(klass.name).replace(' ', '')


