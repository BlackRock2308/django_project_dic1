# Generated by Django 3.2.5 on 2021-07-06 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departements', '0003_auto_20210706_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignantmodel',
            name='password_user',
        ),
        migrations.RemoveField(
            model_name='etudiantmodel',
            name='password_user',
        ),
    ]
