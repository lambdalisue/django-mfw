# Append to the PYTHONPATH
import os, sys
ROOT = os.path.join(os.path.dirname(__file__), '../')

# Activate virtualenv
virtualenv = os.path.join(ROOT, 'env')
if os.path.exists(virtualenv):
    activate_this = os.path.join(virtualenv, "bin/activate_this.py")
    execfile(activate_this, dict(__file__=activate_this))

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
