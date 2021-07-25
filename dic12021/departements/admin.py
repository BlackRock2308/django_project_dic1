from django.contrib import admin
from .models import *
from dic12021.admin import my_admin

# Register your models here.


class DepartementAdmin(admin.ModelAdmin):

    list_display = ("nom", "email", "telephone", "show_nom_email")
    fields = ("nom", ("email", "telephone")) #mail et numero sont affiché sur la meme ligne
    list_editable = ("email",)
    list_per_page = (2)

admin.AdminSite.site_header = "Administration du site de l'EPT"
admin.site.register(DepartementModel, DepartementAdmin, )
admin.site.register(ClasseModel)
admin.site.register(EtudiantModel)
admin.site.register(UniteEnseignementModel)
admin.site.register(MatiereModel)
admin.site.register(InscriptionEleve)
admin.site.register(EnseignantModel )

my_admin.register(DepartementModel)


#Change the navbar dear
#username : mbayecn
#passwword : gnilanesene