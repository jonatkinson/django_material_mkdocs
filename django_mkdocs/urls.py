from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^docs/', include('docs.urls'))
]
