from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from .views import serve_docs

urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Authentication.
    url(r'^accounts/login/', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^accounts/logout/', auth_views.logout, {'template_name': 'logout.html'}, name="logout"),

    # Documentation views.
    url(r'^docs/(?P<path>.*)$', serve_docs, name="serve_docs"),	
    url(r'^$', RedirectView.as_view(url='docs/'), name="home"),
]
