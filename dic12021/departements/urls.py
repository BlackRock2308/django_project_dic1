from departements.serialisers import ViewListEtudiant
from django.urls import path
from .views import * 



urlpatterns = [
    path("departements/git", departementGit, name = "git"),

    path("departement/civil", departementCivil, name = "civil"),
    path("departement/civil/dic1", dic1_civil, name = "dic1_civil"),
    path("departement/civil/dic1/<int:id>/", dic1civil_details, name="dic1civil_details"),
    path("departement/civil/dic2", dic2_civil, name = "dic2_civil"),
    path("departement/civil/dic2/<int:id>/", dic2civil_details, name="dic2civil_details"),
    path("departement/civil/dic3", dic3_civil, name = "dic3_civil"),
    path("departement/civil/dic3/<int:id>/", dic3civil_details, name="dic3civil_details"),
    path("departement/Middle_bar/module_civil", module_civil, name="module_civil"),

    path("departements/meca", departementMeca, name = "meca"),
    path("departements/meca/dic1", dic1_meca, name = "dic1_meca"),
    path("departement/meca/dic1/<int:id>/", dic1meca_details, name="dic1meca_details"),
    path("departements/meca/dic2", dic2_meca, name = "dic2_meca"),
    path("departement/meca/dic2/<int:id>/", dic2meca_details, name="dic2meca_details"),
    path("departements/meca/dic3", dic3_meca, name = "dic3_meca"),
    path("departement/meca/dic3/<int:id>/", dic3meca_details, name="dic3meca_details"),
    path("departement/departements/module_gem", module_gem, name="module_gem"),

    path("departements/aero", departementAero, name = "aero"),
    path("departement/aero/dic1", dic1_aero, name="dic1_aero"),
    path("departement/aero/dic2", dic2_aero, name="dic2_aero"),
    path("departement/aero/dic3", dic3_aero, name="dic3_aero"),
    path("departement/departements/module_aero", module_aero, name="module_aero"),

    path("departement/git/dic1", dic1git, name="dic1git"),
    path("departement/git/dic1/<int:id>/", dic1git_details, name="dic1git_details"),
    path("departement/git/dic2", dic2git, name="dic2git"),
    path("departement/git/dic2/<int:id>/", dic2git_details, name="dic2git_details"),
    path("departement/git/dic3", dic3git, name="dic3git"),
    path("departement/git/dic3/<int:id>/", dic3git_details, name="dic3git_details"),

    path("departement/git/module", module, name="module"),

    path("departement/git/list/", ViewListEtudiant.as_view()),
    path("departement/git/list2/", list_etudiant),
    path("departement/git/list2/<str:depart>/<str:ma_classe>", list_etudiant)
    
]