from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class recruteur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    entreprise = models.CharField(max_length=50)
    liste_secteur = [
        ('Agence pub / Marketing Direct', 'Agence pub / Marketing Direct'),
        ('Agriculture / Environnement', 'Agriculture / Environnement'),
        ('Agroalimentaire', 'Agroalimentaire'),
        ('Ameublement / Décoration', 'Ameublement / Décoration'),
        ('Assurance / Courtage', 'Assurance / Courtage'),
        ('Audiovisuel', 'Audiovisuel'),
        ('Automobile / Motos / Cycles', 'Automobile / Motos / Cycles'),
        ('Autres Industries', 'Autres Industries'),
        ('Autres services', 'Autres services'),
        ('Aéronautique / Spatial', 'Aéronautique / Spatial'),
        ('BTP / Génie Civil', 'BTP / Génie Civil'),
        ('Banque / Finance', 'Banque / Finance'),
        ('Centre d''appel', 'Centre d''appel'),
        ('Chimie / Parachimie / Peintures', 'Chimie / Parachimie / Peintures'),
        ('Communication / Evénementiel', 'Communication / Evénementiel'),
        ('Comptabilité / Audit', 'Comptabilité / Audit'),
        ('Conseil / Etudes', 'Conseil / Etudes'),
        ('Cosmétique / Parfumerie / Luxe', 'Cosmétique / Parfumerie / Luxe'),
        ('Distribution', 'Distribution'),
        ('Edition / Imprimerie', 'Edition / Imprimerie'),
        ('Electricité', 'Electricité'),
        ('Electro-mécanique / Mécanique', 'Electro-mécanique / Mécanique'),
        ('Electronique', 'Electronique'),
        ('Energie', 'Energie'),
        ('Enseignement / Formation', 'Enseignement / Formation'),
        ('Extraction / Mines', 'Extraction / Mines'),
        ('Ferroviaire', 'Ferroviaire'),
        ('Hôtellerie / Restauration', 'Hôtellerie / Restauration'),
        ('Immobilier / Promoteur / Agence', 'Immobilier / Promoteur / Agence'),
        ('Import / Export / Négoce', 'Import / Export / Négoce'),
        ('Informatique', 'Informatique'),
        ('Internet / Multimédia', 'Internet / Multimédia'),
        ('Juridique / Cabinet d’avocats', 'Juridique / Cabinet d’avocats'),
        ('Matériel Médical', 'Matériel Médical'),
        ('Métallurgie / Sidérurgie', 'Métallurgie / Sidérurgie'),
        ('Nettoyage / Sécurité / Gardiennage', 'Nettoyage / Sécurité / Gardiennage'),
        ('Offshoring / Nearshoring', 'Offshoring / Nearshoring'),
        ('Papier / Carton', 'Papier / Carton'),
        ('Pharmacie / Santé', 'Pharmacie / Santé'),
        ('Plasturgie', 'Plasturgie'),
        ('Presse', 'Presse'),
        ('Pétrole / Gaz', 'Pétrole / Gaz'),
        ('Recrutement / Intérim', 'Recrutement / Intérim'),
        ('Service public / Administration', 'Service public / Administration'),
        ('Tabac', 'Tabac'),
        ('Telecom', 'Telecom'),
        ('Textile / Cuir', 'Textile / Cuir'),
        ('Tourisme / Voyage / Loisirs', 'Tourisme / Voyage / Loisirs'),
        ('Transport / Messagerie / Logistique', 'Transport / Messagerie / Logistique')
    ]
    secteur = models.CharField(max_length=50, null=True, choices=liste_secteur)
    logo = models.ImageField(upload_to='logos/%Y/%m/%d/')
    def __str__(self):
        return self.utilisateur.username + ' - ' + self.entreprise

class offre(models.Model):
    titre = models.CharField(max_length=100)
    date_offre = models.DateField(auto_now_add=True)
    experiences = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    telephone = models.CharField(max_length=15)
    date_limite = models.DateField(null=True)
    details = models.TextField()
    rec = models.ForeignKey(recruteur, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.rec.utilisateur.username + ' - offre ' + str(self.id)
    class Meta:
        ordering = ['-date_offre', '-id']
    @property
    def old(self):
        return date.today() > self.date_limite