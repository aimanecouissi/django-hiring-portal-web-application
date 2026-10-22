from django.db import models
from django.contrib.auth.models import User
from recruteur.models import offre

# Create your models here.
class cv(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    cin = models.CharField(max_length=20, null=True, blank=True)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, default='Male')
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    formations = models.TextField()
    competances = models.TextField()
    langues = models.TextField()
    certificats = models.TextField()
    civi = models.FileField(upload_to='cv/%Y/%m/%d/', null=True)
    lettre = models.FileField(upload_to='lettres/%Y/%m/%d/', null=True)
    def __str__(self):
        return self.utilisateur.username

class demande(models.Model):
    date_demande = models.DateField(auto_now_add=True)
    vu = models.BooleanField(default=False)
    etat = models.BooleanField(null=True, blank=True)
    ofr = models.ForeignKey(offre, on_delete=models.CASCADE, null=True)
    dem = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.dem.username + ' - demande ' + str(self.id)
    class Meta:
        ordering = ['-date_demande', '-id']