"""
Unittests for dashboard definitions
"""
from opal.core.test import OpalTestCase

import dashboard

class TestDash(dashboard.Dashboard):
    name = 'The Name'

class DashboardTestCase(OpalTestCase):

    def test_get(self):
        self.assertEqual(TestDash, dashboard.Dashboard.get('the_name'))

    def test_list(self):
        dashes = dashboard.Dashboard.list()
        self.assertEqual([TestDash], dashes)

    def test_slug(self):
        self.assertEqual('the_name', TestDash.slug())
