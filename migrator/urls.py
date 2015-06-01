from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^conf/local/', views.LocalEndpoint, name='localEndpoint'),
    url(r'^conf/remote/', views.RemoteEndpoint, name='remoteEndpoint'),
]
