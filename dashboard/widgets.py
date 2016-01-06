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

    def get_tagline(self):
        return self.tagline

    def get_bg(self):
        return self.bg


class Number(Widget):
    """
    A widget displaying a single number.
    """
    cols     = 'col-md-3'
    template = 'dashboard/widgets/number.html'

    def get_number(self):
        return self.number


class Histogram(Widget):
    """
    A histogram widget
    """
    cols = 'col-md-12'


class Table(Widget):
    """
    A Basic Table
    """
    # assumes the existence in a list/tuple of headers called "table_headers" on the class
    # assumes the existence of "table_data" on the class
    # the data dictionary has the headers as keys
    # it can also include links, these have {{ key__link }} as the name
    # e.g. [
    #    {"bananas": 2, "apples": 4, "apples__link": "http://news.bbc.co.uk"},
    #    {"bananas": 4, "apples": 2, "apples__link": "stuff.com"}
    #  ]
    # ["bananas", "apples"]
    # include index allows you to show the index, e.g. as a ranking
    cols = 'col-md-12'
    template = 'dashboard/widgets/table.html'
    include_index = False
    row_class = "row_class"

    def get_include_index(self):
        return self.include_index

    def get_table_data(self):
        return self.table_data

    def table_iterator(self):
        return [self.get_row(i) for i in self.get_table_data()]

    def get_table_headers(self):
        return self.table_headers

    def get_row(self, dictionary):
        """
        returns an iterator that has a column value associated link if it exists
        """
        headers = self.get_table_headers()
        column_values = [(dictionary.get(h, ''), dictionary.get("%s__link" % h),) for h in headers]
        row_class = dictionary.get(self.row_class, None)
        number = dictionary.get('number', None)
        return dict(column_values=column_values, row_class=row_class, number=number)


class LineChart(Widget):
    """
    A line chart widget
    """
    cols     = 'col-md-12'
    template = 'dashboard/widgets/line.html'

    @classmethod
    def get(cls, name):
        """
        Return a specific ward round by slug
        """
        for sub in cls.__subclasses__():
            if sub.slug == name:
                return sub



"""
Pre-baked usable widgets
"""
class NumberOfUsers(Number):
    tagline = 'Users'

    def get_number(self):
        from django.contrib.auth.models import User
        return User.objects.count()


class NumberOfEpisodes(Number):
    tagline = 'Episodes'

    def get_number(self):
        from opal.models import Episode
        return Episode.objects.count()
