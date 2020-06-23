This is dashboard - an [OPAL](https://github.com/openhealthcare/opal) plugin.


## ! Important Notice !

This plugin is no longer actively maintiained - as it depends on a version of django that is no longer supported by OPAL


[![Build Status](https://travis-ci.org/openhealthcare/opal-dashboard.svg?branch=v0.5.0)](https://travis-ci.org/openhealthcare/opal-dashboard)
[![Coverage Status](https://coveralls.io/repos/github/openhealthcare/opal-dashboard/badge.svg)](https://coveralls.io/github/openhealthcare/opal-dashboard)


Dashboards should be in dashboards.py of your plugin or application.

A dashboard must subclass `dashboard.Dashboard`, and include a number of Widgets -
either `dashboard.widgets.Widget` subclasses, or using one of the pre-built widgets in
`dashboard.widgets`.
