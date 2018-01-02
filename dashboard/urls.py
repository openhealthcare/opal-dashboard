"""
Urls for the dashboard Opal plugin
"""
from django.conf.urls import url

from dashboard import views

urlpatterns = [
    url('^dashboards/$', views.DashboardIndexView.as_view()),
    url('^dashboards/(?P<name>[a-z_-]+)$', views.DashboardView.as_view(), name="dashboard_detail"),
    url('^dashboards/widgets/line-chart/(?P<name>[a-z_-]+)$',
        views.LineChartDataView.as_view()),
]
