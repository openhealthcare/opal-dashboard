"""
Views for the dashboard OPAL Plugin
"""
from django.views.generic import View, TemplateView

from opal.utils.views import LoginRequiredMixin, _build_json_response

class DashboardIndexView(LoginRequiredMixin, TemplateView):
    """
    Main entrypoint into the available dashboards.

    Lists our dashboards.
    """
    template_name = 'dashboard/index.html'

    def get_context_data(self, *args, **kw):
        from dashboard import Dashboard
        
        ctx = super(DashboardIndexView, self).get_context_data(*args, **kw)
        ctx['dashboards'] = Dashboard.list()
        return ctx

class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Render a dashboard.
    """
    template_name = 'dashboard/dashboard.html'

    def dispatch(self, *args, **kw):
        from dashboard import Dashboard
        
        self.dashboard = Dashboard.get(kw['name'])
        return super(DashboardView, self).dispatch(*args, **kw)
    
    def get_context_data(self, *args, **kw):
        ctx = super(DashboardView, self).get_context_data(*args, **kw)
        ctx['dashboard'] = self.dashboard
        return ctx

class LineChartDataView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        from dashboard.widgets import LineChart

        widget = LineChart.get(kwargs['name'])
        return _build_json_response(widget.get_lines())
