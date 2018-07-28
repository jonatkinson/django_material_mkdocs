from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from .views import serve_docs

urlpatterns = [
	
    url(r'^docs/(?P<path>.*)$', serve_docs, name="serve_docs"),	
    url(r'^$', RedirectView.as_view(url='docs/'), name="home"),
]
