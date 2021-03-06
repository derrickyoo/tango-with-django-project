from django.conf.urls import patterns, include, url
# Allows us access to the variables defined within our project's settings.py file
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root':settings.MEDIA_ROOT}),
    )
