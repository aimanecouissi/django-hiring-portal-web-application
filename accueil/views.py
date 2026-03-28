from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from recruteur.models import offre, recruteur
from django.db.models import Count
import math

# Create your views here.
def index(request):
    def millify(n):
        millnames = ['', 'K', 'M', 'B', 'T']
        n = float(n)
        millidx = max(0, min(len(millnames) - 1, int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))
        return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('ajouter')
        else:
            if request.user.username == 'admin':
                auth.logout(request)
                rec = recruteur.objects.all().count()
                dem = User.objects.all().count() - rec - 1
                ofr = offre.objects.all().count()
                data = {
                    'rec':  millify(rec),
                    'dem': millify(dem),
                    'ofr': millify(ofr)           
                }
                return render(request, 'accueil/index.html', data)
            else:
                return redirect('cv')
    else:
        if request.method == 'POST':
            prenom = request.POST['prenom'].capitalize()
            nom = request.POST['nom'].capitalize()
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 != password2:
                messages.error(request, 'Veuillez entrer le même mot de passe.')
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Ce nom d'utilisateur existe déjà.")
                else:
                    if User.objects.filter(email= email).exists():
                        messages.error(request, 'Cet email existe déjà.')
                    else:
                        demandeur = User.objects.create_user(
                            first_name=prenom,
                            last_name=nom,
                            email=email,
                            username=username,
                            password=password1)
                        demandeur.save()
                        prenom = ''
                        nom = ''
                        email = ''
                        username = ''
                        password1 = ''
                        password2 = ''
                        messages.success(request, 'Votre compte a été créé avec succès.')
            rec = recruteur.objects.all().count()
            dem = User.objects.all().count() - rec - 1
            ofr = offre.objects.all().count()
            ofr2 = offre.objects.all()[:3]
            top = list(offre.objects.values('rec').annotate(total=Count('id')).order_by('-total')[:3])
            lst = []
            for l in top:
                lst.append(l['rec'])
            top = recruteur.objects.all().filter(id__in=lst)
            data = {
                'prenom': prenom,
                'nom': nom,
                'email': email,
                'username': username,
                'password1': password1,
                'password2': password2,
                'rec':  millify(rec),
                'dem': millify(dem),
                'ofr': millify(ofr),
                'ofr2': ofr2,
                'top': top  
            }
            return render(request, 'accueil/index.html', data)
        else:
            rec = recruteur.objects.all().count()
            dem = User.objects.all().count() - rec - 1
            ofr = offre.objects.all().count()
            ofr2 = offre.objects.all()[:3]
            top = list(offre.objects.values('rec').annotate(total=Count('id')).order_by('-total')[:3])
            lst = []
            for l in top:
                lst.append(l['rec'])
            top = recruteur.objects.all().filter(id__in=lst)
            data = {
                'rec': millify(rec),
                'dem': millify(dem),
                'ofr': millify(ofr),
                'ofr2': ofr2,
                'top': top  
            }
            return render(request, 'accueil/index.html', data)

def connexion(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('ajouter')
        else:
            return redirect('cv')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            utilisateur = auth.authenticate(username=username, password=password)
            if utilisateur is not None:
                auth.login(request, utilisateur)
                if 'remember' not in request.POST:
                    request.session.set_expiry(0)
                if recruteur.objects.filter(utilisateur=request.user).exists():
                    return redirect('ajouter')
                else:
                    return redirect('cv')
            else:
                messages.error(request, "Le nom d'utilisateur ou le mot de passe sont incorrectes.")
                data = {
                    'username': username,
                    'password': password
                }
                return render(request, 'accueil/connexion.html', data)
        else:
            return render(request, 'accueil/connexion.html')

def deconnexion(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('connexion')