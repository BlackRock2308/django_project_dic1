from django.shortcuts import render
# Create your views here.


def departementGit(request):
    context = {'git': "Code for a better life dear"}
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

