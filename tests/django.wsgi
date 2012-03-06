# Append to the PYTHONPATH
import os, sys
ROOT = os.path.join(os.path.dirname(__file__), '../')

path_list = (
    ROOT,
    os.path.join(ROOT, 'tests', 'src'),
)
for path in path_list:
    if path not in sys.path:
        sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'miniblog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
