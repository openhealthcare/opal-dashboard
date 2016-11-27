"""
Unittests for dashboard
"""
from opal.core.test import OpalTestCase

from dashboard import widgets

class TestWidget(widgets.Widget):
    tagline = 'teh tagline'

class WidgetTestCase(OpalTestCase):

    def test_get_tagline(self):
        self.assertEqual('teh tagline', TestWidget().get_tagline())

    def test_get_bg(self):
        self.assertEqual('active', widgets.Widget().get_bg())
