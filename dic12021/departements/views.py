from django.shortcuts import render, get_list_or_404
from django.contrib import admin
from django.views import generic
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from departements.serialisers import EtudiantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status
from django.utils.translation import gettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@permission_classes(IsAuthenticated,)
@api_view(['GET', "POST","DELETE" ])  # PUT, DELETE etc.
def list_etudiant(request, depart,ma_classe):
    try:
        queryset = EtudiantModel.objects.filter(depart = depart).filter(ma_classe = ma_classe)
    except EtudiantModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #queryset = EtudiantModel.objects.filter(depart = depart).filter(ma_classe = ma_classe)
        serializer = EtudiantSerializer(queryset, many= True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        





# All my views for GIT department

def module(request):
    modules = MatiereModel.objects.filter(classe = "GIT")

    context = {"modules" : modules}
    return render(request, "departements/Middle_bar/module.html", context)



def dic1git(request):
    
    student_list = EtudiantModel.objects.filter(ma_classe = 'DIC1').filter(depart = 'GIT')
    page = request.GET.get('page', 1)
    paginator = Paginator(student_list, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    context = {'students': students, "classe" : "DIC1"}

    return render(request, "departements/dept_git/dic1.html", context)

def dic1git_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC1').filter(depart = 'GIT')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)

def dic2git(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC2').filter(depart = 'GIT')
    context = {'students': students, "classe" : "DIC2"}

    return render(request, "departements/dept_git/dic2.html", context)

def dic2git_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC2').filter(depart = 'GIT')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)

def dic3git(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC3').filter(depart = 'GIT')
    context = {'students': students, "classe" : "DIC3"}

    return render(request, "departements/dept_git/dic3.html", context)

def dic3git_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC3').filter(depart = 'GIT')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)



@login_required(login_url='login')
def departementGit(request):
    departements = DepartementModel.objects.all()
    unite_enseignement = UniteEnseignementModel.objects.all()
    enseignants = EnseignantModel.objects.filter(chief = 'GIT' )
    profs = EnseignantModel.objects.filter(departements = 1) #1 represent
   
    context = {
            "depart":"GIT",
            'enseignants': enseignants, 
            "departements" : departements, 
            "ues":unite_enseignement,
            "profs": profs,
            }
    return render(request, "departements/git.html", context)

def enseignant_git_details(request, id):
    profs = EnseignantModel.objects.filter(departements = 1) #1 represent
    profs = profs.get(id = id)

    context = {
            "profs": profs,
            }
    return render(request, "departements/enseignant_details.html", context)

# End of views for GIT department

# All my views for GEM department

def module_gem(request):
    modules = MatiereModel.objects.filter(classe = "GEM")

    context = {"modules" : modules}
    return render(request, "departements/Middle_bar/module_gem.html", context)


def dic1_meca(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC1').filter(depart = 'GEM')
    context = {'students': students, "classe" : "DIC1"}

    return render(request, "departements/dept_meca/dic1.html", context)

def dic1meca_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC1').filter(depart = 'GEM')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)

def dic2_meca(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC2').filter(depart = 'GEM')
    context = {'students': students, "classe" : "DIC2"}

    return render(request, "departements/dept_meca/dic2.html", context)

def dic2meca_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC2').filter(depart = 'GEM')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)


def dic3_meca(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC3').filter(depart = 'GEM')
    context = {'students': students, "classe" : "DIC3"}

    return render(request, "departements/dept_meca/dic3.html", context)

def dic3meca_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC3').filter(depart = 'GEM')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)

@login_required(login_url='login')
def departementMeca(request):
    departements = DepartementModel.objects.all()
    #unite_enseignement = UniteEnseignementModel.objects.all()
    enseignants = EnseignantModel.objects.filter(chief = 'GEM')
    profs = EnseignantModel.objects.filter(departements = 2) #1 represent
   
    context = {
            "depart" : "ELECTRO-MECANIQUE",
            "departements" : departements, 
            "profs": profs,
            "enseignants" : enseignants,
            }
    return render(request, "departements/meca.html", context)

def enseignant_meca_details(request, id):
    profs = EnseignantModel.objects.filter(departements = 2) #1 represent
    profs = profs.get(id = id)

    context = {
           
            "profs": profs,
            }
    return render(request, "departements/enseignant_details.html", context)

# End of views for GEM department


# All my views for GC department

def module_civil(request):
    modules = MatiereModel.objects.filter(classe = "GC")
    
    context = {"modules" : modules}
    return render(request, "departements/Middle_bar/module_civil.html", context)


def dic1_civil(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC1').filter(depart = 'GC')
    context = {'students': students, "classe" : "DIC1"}

    return render(request, "departements/dept_civil/dic1.html", context)

def dic1civil_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC1').filter(depart = 'GC')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)

def dic2_civil(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC2').filter(depart = 'GC')
    context = {'students': students, "classe" : "DIC2"}

    return render(request, "departements/dept_civil/dic2.html", context)

def dic2civil_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC2').filter(depart = 'GC')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)

def dic3_civil(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC3').filter(depart = 'GC')
    context = {'students': students, "classe" : "DIC3"}

    return render(request, "departements/dept_civil/dic3.html", context)

def dic3civil_details(request, id):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC3').filter(depart = 'GC')
    students = students.get(id = id)
    context = {'students': students}

    return render(request, "departements/student_details.html", context)

@login_required(login_url='login')
def departementCivil(request):
    departements = DepartementModel.objects.all()
    enseignants = EnseignantModel.objects.filter(chief = 'GC')
    profs = EnseignantModel.objects.filter(departements = 3)

    context = {
            "depart" : "GENIE CIVIL",
            "departements" : departements, 
            "profs": profs,
            "enseignants" : enseignants,
            }

    return render(request, "departements/civil.html", context)


# End of views for GC department

# All my views for AERO department

def module_aero(request):
    modules = MatiereModel.objects.filter(classe = "AERO")
    
    context = {"modules" : modules}
    return render(request, "departements/Middle_bar/module_aero.html", context)


def dic1_aero(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC1').filter(depart = 'AERO')
    context = {'students': students}

    return render(request, "departements/dept_aero/dic1.html", context)

def dic2_aero(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC2').filter(depart = 'AERO')
    context = {'students': students}

    return render(request, "departements/dept_aero/dic2.html", context)

def dic3_aero(request):
    
    students = EtudiantModel.objects.filter(ma_classe = 'DIC3').filter(depart = 'AERO')
    context = {'students': students}

    return render(request, "departements/dept_aero/dic3.html", context)

@login_required(login_url='login')
def departementAero(request):
    departements = DepartementModel.objects.all()
    enseignants = EnseignantModel.objects.filter(chief = 'AERO')
    profs = EnseignantModel.objects.filter(departements = 5)

    context = {
            "depart" : "AERONAUTIQUE",
            "departements" : departements, 
            "profs": profs,
            "enseignants" : enseignants,
            }

    return render(request, "departements/aero.html", context)

