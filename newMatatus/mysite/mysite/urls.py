from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^ratings/', include('ratings.urls', namespace="ratings")),
    url(r'^admin/', include(admin.site.urls)),
)