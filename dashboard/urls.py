"""
Urls for the dashboard OPAL plugin
"""
from django.conf.urls import patterns, url

from dashboard import views

urlpatterns = patterns(
    '',
    url('^dashboards/$', views.DashboardIndexView.as_view()),
    url('^dashboards/(?P<name>[a-z_-]+)$', views.DashboardView.as_view()),
    url('^dashboards/widgets/line-chart/(?P<name>[a-z_-]+)$',
        views.LineChartDataView.as_view()),    
)
