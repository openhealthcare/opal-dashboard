"""
Unittests for dashboard
"""
from opal.core.test import OpalTestCase

from dashboard import widgets

class TestWidget(widgets.Widget):
    tagline = 'teh tagline'


class TestNumberWidget(widgets.Number):
    number = 42


class WidgetTestCase(OpalTestCase):

    def test_get_tagline(self):
        self.assertEqual('teh tagline', TestWidget().get_tagline())

    def test_get_bg(self):
        self.assertEqual('active', widgets.Widget().get_bg())


class NumberTestCase(OpalTestCase):

    def test_get_number(self):
        self.assertEqual(42, TestNumberWidget().get_number())


class TableTestCase(OpalTestCase):


    def test_get_include_index(self):
        self.assertEqual(False, widgets.Table().get_include_index())
