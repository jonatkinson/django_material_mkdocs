from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^docs/', include('docs.urls')),
    url(r'^$', RedirectView.as_view(url='docs/')),
    ]
