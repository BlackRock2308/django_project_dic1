from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def departementGit(request):
    departements = DepartementModel.objects.all()
    unite_enseignement = UniteEnseignementModel.objects.all()
    enseignants = EnseignantModel.objects.filter(chef_departement = True)
    
    context = {"depart":"GIT",'enseignants': enseignants, "departements" : departements, "ues":unite_enseignement}
    return render(request, "departements/git.html", context)


def departementMeca(request):
    context = {'mecano': "Mecanichal department for those who like suffering"}
    return render(request, "departements/meca.html", context)


def departementCivil(request):
    context = {'civil': " Civil department for building a better world"}
    return render(request, "departements/civil.html", context)


def departementAero(request):
    context = {'aero': "Welcome to Aero Field in electroMeca department"}
    return render(request, "departements/aero.html", context)

