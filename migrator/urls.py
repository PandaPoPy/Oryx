from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^formulaire_serveur$', views.formulaire_serveur, name='formulaire_serveur'),
    url(r'^login', views.login, name='login'),
]
