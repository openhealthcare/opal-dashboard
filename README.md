This is dashboard - an [OPAL](https://github.com/openhealthcare/opal) plugin.

Dashboards should be in dashboards.py of your plugin or application.

A dashboard must subclass `dashboard.Dashboard`, and include a number of Widgets - 
either `dashboard.widgets.Widget`, or using one of the pre-built widgets in
`dashboard.widgets`.
