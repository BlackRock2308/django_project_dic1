from django.urls import path
from .views import * 



urlpatterns = [
    path("departements/git", departementGit, name = "git"),
    path("departements/civil", departementCivil, name = "civil"),
    path("departements/meca", departementMeca, name = "meca"),
    path("departements/aero", departementAero, name = "aero"),
]