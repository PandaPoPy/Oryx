from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from migrator.forms import LocalEndpointForm, RemoteEndpointForm
from migrator.models import IMAPEndpoint, Migration
from django.conf import settings

# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse('migrator:localEndpoint'))


def local_endpoint(request):
    #Test if the form was sent
    if request.method=="POST":
        form = LocalEndpointForm(request.POST)
        if form.is_valid():
            imap_object=form.save(commit=False)
            imap_object.host_imap=settings.DEFAULT_IMAP_SERVER
            if imap_object.connection():
                imap_object.save()
                request.session['local_endpoint_id']=imap_object.id
                return HttpResponseRedirect(reverse('migrator:remoteEndpoint'))
    else:
        form = LocalEndpointForm()

    return render(request, 'migrator/localendpoint.html', {'form':form})


def remote_endpoint(request):
        #Test if the form was sent
        if request.method=="POST":
            form = RemoteEndpointForm(request.POST)
            if form.is_valid():
                remote_imap=form.save(commit=False)
                if remote_imap.connection():
                    remote_imap.save()
                    if 'local_endpoint_id' in request.session:
                        local_endpoint_id = request.session['local_endpoint_id']
                        local_imap= IMAPEndpoint.objects.get(id=local_endpoint_id)
                        migration= Migration(origin = local_imap, target = remote_imap)
                        migration.save()
                        return render(request, 'migrator/recap.html', {'migration': migration})
        else:
            form = RemoteEndpointForm()

        return render(request, 'migrator/localendpoint.html', {'form':form})


def recap(request):
    return render(request, 'migrator/recap.html')