from typing import Text
from django.db import models
from django.contrib.auth.models import User
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

    class Meta :
        verbose_name = "Classe"
       


class UniteEnseignementModel(models.Model):
    code_ue = models.CharField(max_length=300,unique=True, null=True)
    nom_ue = models.CharField(max_length=300, null=True)
    id_classe = models.ForeignKey(ClasseModel, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.nom_ue

    class Meta :
        verbose_name = "Unité d'Enseignement"
        verbose_name_plural = "Unités d'Enseignement"
    

class MatiereModel(models.Model):
    CATEGORY = (
            ('GIT', 'GIT'),
            ('GEM', 'GEM'),
            ('AERO', 'AERO'),
            ('GC', 'GC'),
            ('TC', 'TC')
        )
    code_matiere = models.CharField(max_length=300,unique=True)
    nom_matiere = models.CharField(max_length=300)
    coefficient = models.IntegerField(null=True)
    credit_matiere = models.IntegerField(null= True)
    quota_horaire = models.IntegerField(null= True)
    description_matiere = models.TextField(null= True)
    unite_enseignement = models.ForeignKey(UniteEnseignementModel, on_delete=models.CASCADE)
    classe = models.CharField(max_length = 200, null = True, choices = CATEGORY)


    def __str__(self) -> str:
        return self.nom_matiere

    class Meta :
        verbose_name = "Matiere"


class Utilisateur(models.Model):  # COMM0N
    #user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    mail_user =  models.EmailField(max_length=300, null= True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
  
    class Meta:
        abstract = True


class EtudiantModel(Utilisateur):  # STUDENT
    CATEGORY = (
            ('GIT', 'GIT'),
            ('GEM', 'GEM'),
            ('GC', 'GC'),
            ('AERO', 'AERO'),
            ('TC', 'TC')
        )
    LEVEL = (
            ('TC1', 'TC1'),
            ('TC2', 'TC2'),
            ('DIC1', 'DIC1'),
            ('DIC2', 'DIC2'),
            ('DIC3', 'DIC3')
        )
    #user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=300, null=True)
    depart = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    ma_classe = models.CharField(max_length = 200, null = True, choices = LEVEL )
    
    class Meta :
        verbose_name = "Etudiant"

  
class EnseignantModel(Utilisateur):  # TEACHER
    CATEGORY = (
            ('GIT', 'GIT'),
            ('GEM', 'GEM'),
            ('GC', 'GC'),
            ('AERO', 'AERO'),
            ('TC', 'TC'),
            ('----', '----')
        )
    contact_prof = models.CharField(max_length=150)
    date_adhesion = models.DateField(null= True)
    chef_departement = models.BooleanField(default=False)
    departements = models.ManyToManyField(DepartementModel)
    matieres = models.ManyToManyField(MatiereModel)
    chief = models.CharField(max_length = 200, null = True, choices = CATEGORY)

    class Meta :
        verbose_name = "Enseignant"


class InscriptionEleve(models.Model):
    Id_etudiant = models.ForeignKey(EtudiantModel, on_delete= models.CASCADE)
    Id_classe = models.ForeignKey(ClasseModel, on_delete=models.CASCADE)
    annee_scolaire = models.CharField(max_length=300, null=True, default="2020-2021")

    def __str__(self) -> str:
        return f"{self.Id_etudiant} {self.annee_scolaire} " 






   
    
    


