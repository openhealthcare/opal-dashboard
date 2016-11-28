"""
Unittests for dashboard views
"""
from opal.core.test import OpalTestCase

from dashboard import views

from dashboard.tests.test_dashboards import TestDash

class DashboardIndexViewTestCase(OpalTestCase):

    def setup_view(self, view):
        v = view()
        r = self.rf.get('hah.html')
        v.request = r
        return v

    def test_get_context_data(self):
        view = self.setup_view(views.DashboardIndexView)
        ctx = view.get_context_data()
        self.assertEqual([TestDash], ctx['dashboards'])
