# Generated by Django 3.2.5 on 2021-07-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departements', '0013_inscriptioneleve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptioneleve',
            name='annee_scolaire',
            field=models.CharField(default='2020-2021', max_length=300, null=True),
        ),
    ]
