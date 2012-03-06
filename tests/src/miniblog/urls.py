from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', include('django.contrib.auth.urls')),
    url(r'^', include('miniblog.blogs.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
