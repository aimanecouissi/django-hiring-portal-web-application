from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
]