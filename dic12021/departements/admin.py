from django.contrib import admin

from .models import DepartementModel

# Register your models here.


class DepartementAdmin(admin.ModelAdmin):

    list_display = ("nom", "email", "telephone", "show_nom_email")
    fields = ("nom", ("email", "telephone")) #mail et numero sont affiché sur la meme ligne
    list_editable = ("email",)
    list_per_page = (2)

admin.AdminSite.site_header = "Administration du site de l'EPT"
admin.site.register(DepartementModel, DepartementAdmin, )

#Change the navbar dear