"""
Unittests for dashboard views
"""
import json

from opal.core.test import OpalTestCase
from mock import patch, MagicMock

from dashboard import views

from dashboard.tests.test_dashboards import TestDash

class ViewTestCase(OpalTestCase):

    def setup_view(self, view):
        v = view()
        r = self.rf.get('hah.html')
        v.request = r
        v.request.user = MagicMock(name='Mock User')
        return v


class DashboardIndexViewTestCase(ViewTestCase):

    def test_get_context_data(self):
        view = self.setup_view(views.DashboardIndexView)
        ctx = view.get_context_data()
        self.assertEqual([TestDash], list(ctx['dashboards']))


class DashboardViewTestCase(ViewTestCase):

    def test_dispatch(self):
        view = self.setup_view(views.DashboardView)
        view.dispatch(view.request, name='the_name')
        self.assertEqual(TestDash, view.dashboard)

    def test_get_context_data(self):
        view = self.setup_view(views.DashboardView)
        view.dashboard = TestDash
        ctx = view.get_context_data()
        self.assertEqual(TestDash, ctx['dashboard'])


class LineChartViewTestCase(ViewTestCase):

    @patch('dashboard.widgets.LineChart')
    def test_get(self, line_chart):
        line_chart.get.return_value.return_value.get_lines.return_value = [[],[]]
        view = self.setup_view(views.LineChartDataView)
        resp = view.get(view.request, name='the_chart')
        self.assertEqual([[], []], json.loads(resp.content))
