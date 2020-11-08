from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import re_path, include, path

admin.autodiscover()


urlpatterns = [
    path('', include('bridgenet_payment.apps.core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG_STATIC_FILES:
    urlpatterns += [re_path(r'^devstatic/(?P<path>.*)$', serve)]
