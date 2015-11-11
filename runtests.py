"""
Standalone test runner for Dashboards plugin
"""
import os
import sys

from django.conf import settings

from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'opal.tests.dummy_opal_application'


settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   OPAL_OPTIONS_MODULE = 'dashboard.tests.dummy_options_module',
                   ROOT_URLCONF='dashboard.urls',
                   COMPRESS_ROOT='/tmp/',
                   STATIC_URL = '/assets/',
                   MIDDLEWARE_CLASSES = (
                       'django.middleware.common.CommonMiddleware',
                       'django.contrib.sessions.middleware.SessionMiddleware',
                       'opal.middleware.AngularCSRFRename',
                       'django.middleware.csrf.CsrfViewMiddleware',
                       'django.contrib.auth.middleware.AuthenticationMiddleware',
                       'django.contrib.messages.middleware.MessageMiddleware',
                       'opal.middleware.DjangoReversionWorkaround',
                       'reversion.middleware.RevisionMiddleware',
                       'axes.middleware.FailedLoginMiddleware',
                   ),
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'django.contrib.staticfiles',
                                   'compressor',
                                   'opal',
                                   'opal.tests',
                                   'dashboard',),)

from dashboard.tests import dummy_options_module

import django
django.setup()


from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['dashboard', ])
if failures:
    sys.exit(failures)
