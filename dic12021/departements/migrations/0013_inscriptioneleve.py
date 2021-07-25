# Generated by Django 3.2.5 on 2021-07-13 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departements', '0012_auto_20210712_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='InscriptionEleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_scolaire', models.DateField(null=True)),
                ('Id_classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departements.classemodel')),
                ('Id_etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departements.etudiantmodel')),
            ],
        ),
    ]