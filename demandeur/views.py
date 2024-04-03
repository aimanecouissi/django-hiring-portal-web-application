from django.shortcuts import get_object_or_404, render, redirect
from recruteur.models import recruteur, offre
from .models import cv, demande
from django.contrib import messages, auth
from datetime import datetime

# Create your views here.
def CV(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('index')
        if request.user.username == 'admin':
            auth.logout(request)
            return redirect('/')
        if cv.objects.filter(utilisateur=request.user).exists():
            mycv = cv.objects.get(utilisateur=request.user)
            if request.method == 'POST':
                if len(request.FILES) != 0:
                    if 'photo' in request.FILES:
                        mycv.photo = request.FILES['photo']
                    if 'civi' in request.FILES:
                        mycv.civi = request.FILES['civi']
                    if 'lettre' in request.FILES:
                        mycv.lettre = request.FILES['lettre']
                mycv.cin = request.POST['cin']
                mycv.date_naissance = datetime.fromisoformat(request.POST['date_naissance'])
                mycv.sexe = request.POST['sexe']
                mycv.adresse = request.POST['adresse']
                request.user.email = request.POST['email']
                mycv.telephone = request.POST['telephone']
                mycv.formations = request.POST['formations']
                mycv.competances = request.POST['competances']
                mycv.langues = request.POST['langues']
                mycv.certificats = request.POST['certificats']
                mycv.save()
            sexeF = None
            sexeM = None
            if mycv.sexe == 'Male':
                sexeM = 'Selected'
            else:
                sexeF = 'Selected'
            data = {
                'photo': mycv.photo,
                'cin': mycv.cin,
                'nom_prenom': request.user.last_name + ' ' + request.user.first_name,
                'date_naissance': mycv.date_naissance.strftime('%Y-%m-%d'),
                'sexeM': sexeM,
                'sexeF': sexeF,
                'adresse': mycv.adresse,
                'email': request.user.email,
                'telephone': mycv.telephone,
                'formations': mycv.formations,
                'competances': mycv.competances,
                'langues': mycv.langues,
                'certificats': mycv.certificats,
                'civi': mycv.civi,
                'lettre': mycv.lettre,
                'required': ''
            }
            return render(request, 'demandeur/cv.html', data)
        else:
            if request.method == 'POST':
                mycv = cv(
                    utilisateur=request.user,
                    photo=request.FILES['photo'],
                    cin=request.POST['cin'],
                    date_naissance=request.POST['date_naissance'],
                    sexe=request.POST['sexe'],
                    adresse=request.POST['adresse'],
                    telephone=request.POST['telephone'],
                    formations=request.POST['formations'],
                    competances=request.POST['competances'],
                    langues=request.POST['langues'],
                    certificats=request.POST['certificats'],
                    civi=request.FILES['civi'],
                    lettre=request.FILES['lettre']
                )
                mycv.save()
                return redirect('cv')
            data = {
                'nom_prenom': request.user.last_name + ' ' + request.user.first_name,
                'email': request.user.email,
                'required': 'required'
            }
            return render(request, 'demandeur/cv.html', data)
    else:
        return redirect('index')

def offres(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('index')
        if request.user.username == 'admin':
            auth.logout(request)
            return redirect('/')
        ofr = offre.objects.all()
        if len(ofr) == 0:
            messages.info(request, "Désolè, pas d'offres pour le moment.")
        else:
            if 'recruteur' in request.GET:
                srec = request.GET['recruteur']
                if srec:
                    r = recruteur.objects.all().filter(entreprise__icontains=srec)
                    ofr = ofr.filter(rec__in=r)
            if 'secteur' in request.GET:
                ssec = request.GET['secteur']
                if ssec:
                    r = recruteur.objects.all().filter(secteur__icontains=ssec)
                    ofr = ofr.filter(rec__in=r)
            if 'ville' in request.GET:
                svil = request.GET['ville']
                if svil:
                    ofr = ofr.filter(adresse__icontains=svil)
            if 'mot' in request.GET:
                smot = request.GET['mot']
                if smot:
                    ofr = ofr.filter(details__icontains=smot)
            if 'date' in request.GET:
                sdate = request.GET['date']
                if sdate:
                    ofr = ofr.filter(date_offre=sdate)
            if len(ofr) == 0:
                messages.info(request, "Désolè, pas d'offres pour cette recherche.")
        data = {
            'demande': demande.objects.all().filter(dem = request.user),
            'offre': ofr
        }
        return render(request, 'demandeur/offres.html', data)
    else:
        return redirect('index')

def Offre(request, id_offre):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('index')
        if request.user.username == 'admin':
            auth.logout(request)
            return redirect('/')
        dis = ''
        if demande.objects.filter(dem_id=request.user.id, ofr_id=id_offre).exists():
            messages.info(request, 'Vous avez déjà choisi cet offre.')
        if request.method == 'POST':
            if not cv.objects.filter(utilisateur=request.user).exists():
                messages.warning(request, 'Veuillez remplir votre CV avant de postuler.')
            else:
                dmd = demande(
                    ofr=offre.objects.get(id=id_offre),
                    dem=request.user
                )
                dmd.save()
                messages.success(request, 'Votre demande a été envoyée avec succès.')
                dis = 'disabled'
        if demande.objects.filter(dem_id=request.user.id, ofr_id=id_offre).exists():
            dis = 'disabled'
        data = {
            'offre': get_object_or_404(offre, pk=id_offre),
            'dis': dis
        }
        return render(request, 'demandeur/offre.html', data)
    else:
        return redirect('index')

def demandes(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('index')
        if request.user.username == 'admin':
            auth.logout(request)
            return redirect('/')
        dmd = demande.objects.filter(dem=request.user).all()
        if request.method == 'GET':
            if 'valide' in request.GET:
                dmd = dmd.filter(etat=True)
                if len(dmd) == 0:
                    messages.info(request,"Vous n'avez aucune demande validée.")
            elif 'cours' in request.GET:
                dmd = dmd.filter(etat=None)
                if len(dmd) == 0:
                    messages.info(request,"Vous n'avez aucune demande en cours.")
            elif 'rejete' in request.GET:
                dmd = dmd.filter(etat=False)
                if len(dmd) == 0:
                    messages.info(request,"Vous n'avez aucune demande rejetée.")
            else:
                if len(dmd) == 0:
                    messages.info(request,"Vous n'avez fait aucune demande.")
        return render(request, 'demandeur/demandes.html', {'demande': dmd})
    else:
        return redirect('index')

def Demande(request, id_demande):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('/')
        if request.user.username == 'admin':
            auth.logout(request)
            return redirect('/')
        if request.method == 'POST':
            dmd = demande.objects.get(id=id_demande)
            dmd.delete()
            return redirect('demandes2')
        return render(request, 'demandeur/demande.html', {'demande': get_object_or_404(demande, pk=id_demande)})
    else:
        return redirect('index')

def parametres(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            return redirect('/')
        if request.user.username == 'admin':
            auth.logout(request)
            return redirect('/')
        if request.method == 'POST':
            request.user.first_name = request.POST['prenom']
            request.user.last_name = request.POST['nom']
            request.user.email = request.POST['email']
            request.user.username = request.POST['username']
            request.user.set_password(request.POST['password']) 
            request.user.save()
            auth.login(request, request.user)
            messages.success(request, 'Vos informations on été mise à jour.')
            return redirect('parametres2')
        else:
            return render(request, 'demandeur/parametres.html')
    else:
        return redirect('index')