#!/usr/bin/env python

import os
import sys
root = os.path.dirname(__file__)
if root not in sys.path:
    sys.path.insert(0, root)

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'

def run_tests(verbosity=1):
    from django.test.simple import DjangoTestSuiteRunner
    runner = DjangoTestSuiteRunner(verbosity=verbosity)
    return runner.run_tests(['test_override_settings'])

if __name__ == '__main__':
    run_tests()
