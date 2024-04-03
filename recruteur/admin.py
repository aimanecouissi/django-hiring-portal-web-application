from django.contrib import admin
from .models import recruteur, offre

class recruteurAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'entreprise', 'secteur']
    search_fields = ['utilisateur__username']
    list_filter = ['secteur']

class offreAdmin(admin.ModelAdmin):
    list_display = ['rec', 'titre', 'date_limite']
    search_fields = ['rec__utilisateur__username']

# Register your models here.
admin.site.register(recruteur, recruteurAdmin)
admin.site.register(offre, offreAdmin)