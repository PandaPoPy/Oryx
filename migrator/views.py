from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from migrator.forms import Local_Endpoint, Remote_Endpoint

# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse('migrator:localEndpoint'))


def LocalEndpoint(request):
    #Test if the form was sent
    if request.method=="POST":
        form = Local_Endpoint(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('migrator:remoteEndpoint'))
    else:
        form = Local_Endpoint()
        return render(request, 'migrator/localendpoint.html', {'form':form})


def RemoteEndpoint(request):
    #Test if the form was sent
    if request.method=="POST":
        form = Remote_Endpoint(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('migrator: localEndpoint'))
    else:
        form = Remote_Endpoint()
        return render(request, 'migrator/remoteendpoint.html', {'form':form})
