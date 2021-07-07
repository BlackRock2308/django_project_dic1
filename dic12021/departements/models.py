from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import OneToOneField


# Create your models here.

class DepartementModel(models.Model):
    nom = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=300)
    telephone = models.CharField(max_length=150)
    description_dept = models.TextField()

    def __str__(self):
        return self.nom

    def show_nom_email(self):
        return f"{self.nom}: {self.email}"

    class Meta :
        verbose_name = "département"
        verbose_name_plural = "départements"


class ClasseModel(models.Model):
    nom_classe = models.CharField(max_length=300, null=True)
    description_classe = models.TextField()
    departement = models.ForeignKey(DepartementModel, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nom_classe} {self.departement}"


class UniteEnseignementModel(models.Model):
    code_ue = models.CharField(max_length=300,unique=True, null=True)
    nom_ue = models.CharField(max_length=300, null=True)
    id_classe = models.ForeignKey(ClasseModel, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.nom_ue
    

class MatiereModel(models.Model):
    code_matiere = models.CharField(max_length=300,unique=True)
    nom_matiere = models.CharField(max_length=300)
    coefficient = models.IntegerField(null=True)
    credit_matiere = models.IntegerField(null= True)
    quota_horaire = models.IntegerField(null= True)
    description_matiere = models.TextField(null= True)
    unite_enseignement = models.ForeignKey(UniteEnseignementModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom_matiere


class Utilisateur(models.Model):  # COMM0N
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    mail_user =  models.EmailField(max_length=300, null= True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
  
    class Meta:
        abstract = True


class EtudiantModel(Utilisateur):  # STUDENT
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=300, null=True)

  
class EnseignantModel(Utilisateur):  # TEACHER
    contact_prof = models.CharField(max_length=150)
    date_adhesion = models.DateField(null= True)
    chef_departement = models.BooleanField(default=False)
    departements = models.ManyToManyField(DepartementModel)
    matieres = models.ManyToManyField(MatiereModel)


class InscriptionEleve(models.Model):
    Id_etudiant = models.ForeignKey(EtudiantModel, on_delete= models.CASCADE)
    Id_classe = models.ForeignKey(ClasseModel, on_delete=models.CASCADE)
    annee_scolaire = models.DateField()

    def __str__(self) -> str:
        return self.annee_scolaire






   
    
    


