from django.contrib import admin
from .models import cv, demande

admin.site.site_header = 'Administration de Wadifati'
admin.site.site_title = 'Administration de Wadifati'

class demandeAdmin(admin.ModelAdmin):
    list_display = ['dem', 'ofr', 'etat', 'date_demande']
    search_fields = ['dem__username']
    list_filter = ['etat']

class cvAdmin(admin.ModelAdmin):
    search_fields = ['utilisateur__username']
    list_filter = ['sexe']

# Register your models here.
admin.site.register(cv, cvAdmin)
admin.site.register(demande, demandeAdmin)