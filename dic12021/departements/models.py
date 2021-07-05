from typing import Text
from django.db import models

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
    


