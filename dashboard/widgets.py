"""
Widget definitions for the OPAL dashboard plugin
"""
import json

class Widget(object):
    """
    Base Widget class
    """
    cols = 'col-md-4'
    bg   = 'active'

    @classmethod
    def get_tagline(kls):
        return kls.tagline

    @classmethod
    def get_bg(kls):
        return kls.bg
    
    
class Number(Widget):
    """
    A widget displaying a single number.
    """
    cols     = 'col-md-3'
    template = 'dashboard/widgets/number.html'

    @classmethod
    def get_number(kls):
        return kls.number


class Histogram(Widget):
    """
    A histogram widget
    """
    cols = 'col-md-12'


class LineChart(Widget):
    """
    A line chart widget
    """
    cols     = 'col-md-12'
    template = 'dashboard/widgets/line.html'

    @classmethod
    def get(klass, name):
        """
        Return a specific ward round by slug
        """
        for sub in klass.__subclasses__():
            if sub.slug == name:
                return sub
            
    

"""
Pre-baked usable widgets
"""
class NumberOfUsers(Number):
    tagline = 'Users'
    
    @classmethod
    def get_number(kls):
        from django.contrib.auth.models import User
        return User.objects.count()


class NumberOfEpisodes(Number):
    tagline = 'Episodes'
    
    @classmethod
    def get_number(kls):
        from opal.models import Episode
        return Episode.objects.count()
