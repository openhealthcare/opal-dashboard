"""
Unittests for dashboard templatetags
"""
from opal.core.test import OpalTestCase

from dashboard.templatetags import dashboards

class DashboardWidgetTestCase(OpalTestCase):
    def test_dashboard_widget(self):
        self.assertEqual({'widget': 'line'}, dashboards.dashboard_widget('line'))
