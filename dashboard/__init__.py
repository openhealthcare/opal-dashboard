from django.conf import settings

from opal.utils import stringport, camelcase_to_underscore

from dashboard import plugin # Don't do this once we've updated plugins in Opal

# So we only do it once
IMPORTED_FROM_APPS = False

def import_from_apps():
    """
    Iterate through installed apps attempting to import app.wardrounds
    This way we allow our implementation, or plugins, to define their
    own ward rounds.
    """
    global IMPORTED_FROM_APPS
    if IMPORTED_FROM_APPS:
        return
    for app in settings.INSTALLED_APPS:
        try:
            stringport(app + '.dashboards')
        except ImportError:
            pass # not a problem
    IMPORTED_FROM_APPS = True
    return

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
        import_from_apps()

        for sub in klass.__subclasses__():
            if sub.slug() == name:
                return sub

    @classmethod
    def list(klass):
        """
        Return a list of all ward rounds
        """
        import_from_apps()
        return klass.__subclasses__()

    @classmethod
    def slug(klass):
        return camelcase_to_underscore(klass.name).replace(' ', '')
