from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from migrator.forms import LocalEndpointForm, RemoteEndpointForm

# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse('migrator:localEndpoint'))


def LocalEndpoint(request):
    #Test if the form was sent
    if request.method=="POST":
        form = LocalEndpointForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('migrator:remoteEndpoint'))
    else:
        form = LocalEndpointForm()

    return render(request, 'migrator/localendpoint.html', {'form':form})


def RemoteEndpoint(request):
    #Test if the form was sent
    if request.method=="POST":
        form = RemoteEndpointForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('migrator: localEndpoint'))
    else:
        form = RemoteEndpointForm()

    return render(request, 'migrator/remoteendpoint.html', {'form':form})
