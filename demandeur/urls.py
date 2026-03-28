from django.urls import path
from . import views

urlpatterns = [
    path('', views.CV, name='cv'),
    path('offres', views.offres, name='offres2'),
    path('offre/<int:id_offre>', views.Offre, name='offre2'),
    path('demandes', views.demandes, name='demandes2'),
    path('demande/<int:id_demande>', views.Demande, name='demande2'),
    path('parametres', views.parametres, name='parametres2'),
]