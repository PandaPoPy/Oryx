from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def login(request):
    #teste si formulaire a été envoyé
    if len(request.POST)>0:
        #teste si les paramètres attendus ont été transmis
        if 'email' not in request.POST or 'password' not in request.POST:
            error = "Veuillez entrer une adresse de courriel et un mot de passe."
            return render_to_response('migrator/index.html', {'error': error})
        else:
            email = request.POST['email']
            password = request.POST['password']
            #teste si le mot de passe est le bon
            if password != 'yop' or email != 'contact@example.com':
                error = "Adresse email ou mot de passe erroné."
                return render_to_response('migrator/index.html', {'error': error})
            #tout est bon, on va sur la page suivante
            else:
                return HttpResponseRedirect(reverse('migrator:formulaire_serveur'))
    #le formualaire n'a pas été envoyé
    else:
        return render(request, 'migrator/index.html')


def formulaire_serveur(request):
    return render(request, 'migrator/formulaire_serveur.html')