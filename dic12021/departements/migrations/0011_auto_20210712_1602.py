# Generated by Django 3.2.5 on 2021-07-12 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departements', '0010_rename_departement_etudiantmodel_depart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscriptioneleve',
            name='Id_etudiant',
        ),
        migrations.DeleteModel(
            name='EtudiantModel',
        ),
    ]
