from django.urls import path
from . import views

urlpatterns = [
    path('', views.ajouter, name = 'ajouter'),
    path('demandes', views.demandes, name = 'demandes'),
    path('demande/<int:id_demande>', views.Demande, name = 'demande'),
    path('offres', views.offres, name = 'offres'),
    path('offre/<int:id_offre>', views.Offre, name = 'offre'),
    path('parametres', views.parametres, name = 'parametres'),
]