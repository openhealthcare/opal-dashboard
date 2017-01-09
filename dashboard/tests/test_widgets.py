"""
Unittests for dashboard
"""
from opal.core.test import OpalTestCase

from dashboard import widgets

class TestWidget(widgets.Widget):
    tagline = 'teh tagline'


class TestNumberWidget(widgets.Number):
    number = 42


class TestLineChart(widgets.LineChart):
    slug = 'tester'


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

    def test_get_table_data(self):
        class MyTable(widgets.Table):
            table_data = []

        self.assertEqual([], MyTable().get_table_data())

    def test_table_iterator(self):
        class MyTable(widgets.Table):
            table_data = []

        self.assertEqual([], MyTable().table_iterator())

    def test_get_table_headers(self):
        class MyTable(widgets.Table):
            table_headers = []

        self.assertEqual([], MyTable().get_table_headers())

    def test_get_row(self):
        class MyTable(widgets.Table):
            table_headers = {}

        self.assertEqual({'column_values': [], 'number': None, 'row_class': None},
                         MyTable().get_row({}))


class LineChartTestCase(OpalTestCase):

    def test_get(self):
        self.assertEqual(TestLineChart, widgets.LineChart.get('tester'))


class NumberOfUsersTestCase(OpalTestCase):

    def test_get_number(self):
        self.assertEqual(0, widgets.NumberOfUsers().get_number())


class NumberOfEpisodesTestCase(OpalTestCase):

    def test_get_number(self):
        self.assertEqual(0, widgets.NumberOfEpisodes().get_number())
