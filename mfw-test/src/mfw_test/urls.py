from django.conf.urls.defaults import *
from django.conf import settings
import os.path

urlpatterns = patterns('',
    url(r'^$',                         'mfw_test.index.views.index'),
)
#urlpatterns += patterns('django.views.static',
#    url(r'^image/(P<path>.*)$',    'serve',    kwargs={
#        'document_root': os.path.join(settings.ROOT, 'statics/image'),
#    })
#)