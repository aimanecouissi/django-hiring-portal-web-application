from asyncio.windows_events import NULL
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from recruteur.models import recruteur, offre
from django.contrib import messages, auth
from demandeur.models import cv, demande
from django.contrib.auth.models import User

# Create your views here.
def ajouter(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            if request.method == 'POST':
                r = recruteur.objects.get(utilisateur_id=request.user)
                ofr = offre(
                    rec=r,
                    titre=request.POST['titre'],
                    experiences=request.POST['experiences'],
                    niveau=request.POST['niveau'],
                    adresse=request.POST['adresse'],
                    email=request.POST['email'],
                    telephone=request.POST['telephone'],
                    date_limite=request.POST['dl'],
                    details=request.POST['details']
                )
                ofr.save()
                messages.success(request, 'Votre offre a été ajouté avec succès.')
            data = {
                'nrec': recruteur.objects.get(utilisateur=request.user),
                'datenow': date.today().strftime('%Y-%m-%d')
            }
            return render(request, 'recruteur/ajouter.html', data)
        return redirect('index')
    else:
        return redirect('index')

def demandes(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            r = recruteur.objects.get(utilisateur=request.user)
            o = offre.objects.all().filter(rec=r)
            dmd = demande.objects.all().filter(ofr__in=o)
            if request.method == 'GET':
                if 'nom' in request.GET:
                    snom = request.GET['nom']
                    if snom:
                        dmr = User.objects.all().filter(last_name__icontains=snom)
                        dmd = dmd.filter(dem__in=dmr)
                if 'prenom' in request.GET:
                    spre = request.GET['prenom']
                    if spre:
                        dmr = User.objects.all().filter(first_name__icontains=spre)
                        dmd = dmd.filter(dem__in=dmr)
                if 'titre' in request.GET:
                    stit = request.GET['titre']
                    if stit:
                        of = offre.objects.all().filter(titre__icontains=stit)
                        dmd = dmd.filter(ofr__in=of)
                if 'date' in request.GET:
                    sdate = request.GET['date']
                    if sdate:
                        dmd = dmd.filter(date_demande=sdate)
                rech = None
                if len(dmd) == 0:
                    rech = "Désolè, pas de demande pour cette recherche."
                if 'valide' in request.GET:
                    dmd = dmd.filter(etat=True)
                    if len(dmd) == 0:
                        messages.info(request, "Vous n'avez validé aucune demande.")
                elif 'cours' in request.GET:
                    dmd = dmd.filter(etat=None)
                    if len(dmd) == 0:
                        messages.info(request, "Vous n'avez aucune demande en cours.")
                elif 'rejete' in request.GET:
                    dmd = dmd.filter(etat=False)
                    if len(dmd) == 0:
                        messages.info(request, "Vous n'avez rejeté aucune demande.")
                else:
                    if len(dmd) == 0:
                        if rech:
                            messages.info(request, rech)
                        else:
                            messages.info(request, "Vous n'avez reçu aucune demande pour le moment.")
            data = {
                'demande': dmd,
                'nrec': recruteur.objects.get(utilisateur=request.user)
            }
            return render(request, 'recruteur/demandes.html', data)
        return redirect('index')
    else:
        return redirect('index')

def Demande(request, id_demande):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            dmd = get_object_or_404(demande, pk=id_demande)
            dmd.vu = True
            dmd.save()
            msg = ''
            if dmd.etat == True:
                msg = 'Vous avez déjà validé cette demande.'
            if dmd.etat == False:
                msg = 'Vous avez déjà rejeté cette demande.'
            if request.method == 'POST':
                if 'valider' in request.POST:
                    if dmd.etat == True:
                        msg = 'Vous avez déjà validé cette demande.'
                    else:
                        dmd.etat = True
                        dmd.save()
                        msg = 'Cette demande a été validée.'
                if 'rejeter' in request.POST:
                    if dmd.etat == False:
                        msg = 'Vous avez déjà rejeté cette demande.'
                    else:
                        dmd.etat = False
                        dmd.save()
                        msg = 'Cette demande a été rejetée.'
            messages.info(request, msg)
            mycv = cv.objects.get(utilisateur=dmd.dem)
            data = {
                'demande': dmd,
                'cv': mycv,
                'nrec': recruteur.objects.get(utilisateur=request.user)
            }
            return render(request, 'recruteur/demande.html', data)
        return redirect('index')
    else:
        return redirect('index')

def offres(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            r = recruteur.objects.get(utilisateur=request.user)
            ofr = offre.objects.all().filter(rec=r)
            if len(ofr) == 0:
                messages.info(request, "Vous n'avez ajouté aucun offre jusqu'à maintenant.")
            else:
                if 'titre' in request.GET:
                    stit = request.GET['titre']
                    if stit:
                        ofr = ofr.filter(titre__icontains=stit)
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
                'offres': ofr,
                'nrec': recruteur.objects.get(utilisateur=request.user)
            }
            return render(request, 'recruteur/offres.html', data)
        return redirect('index')
    else:
        return redirect('index')

def Offre(request, id_offre):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            if request.method == 'POST':
                ofr = offre.objects.get(id=id_offre)
                if 'modifier' in request.POST:
                    ofr.titre = request.POST['titre']
                    ofr.experiences = request.POST['experiences']
                    ofr.niveau = request.POST['niveau']
                    ofr.adresse = request.POST['adresse']
                    ofr.email = request.POST['email']
                    ofr.telephone = request.POST['telephone']
                    ofr.date_limite = request.POST['dl']
                    ofr.details = request.POST['details']
                    ofr.save()
                if 'supprimer' in request.POST:
                    ofr.delete()
                    return redirect('offres')
            date = offre.objects.get(id=id_offre).date_offre.strftime('%Y-%m-%d')
            date2 = offre.objects.get(id=id_offre).date_limite.strftime('%Y-%m-%d')
            data = {
                'offre': get_object_or_404(offre, pk=id_offre),
                'date': date,
                'date2': date2,
                'nrec': recruteur.objects.get(utilisateur=request.user)
            }
            return render(request, 'recruteur/offre.html', data)
        return redirect('index')
    else:
        return redirect('index')

def parametres(request):
    if request.user.is_authenticated:
        if recruteur.objects.filter(utilisateur=request.user).exists():
            if request.method == 'POST':
                request.user.first_name = request.POST['prenom']
                request.user.last_name = request.POST['nom']
                request.user.email = request.POST['email']
                request.user.username = request.POST['username']
                request.user.set_password(request.POST['password']) 
                request.user.save()
                auth.login(request, request.user)
                messages.success(request, 'Vos informations on été mise à jour.')
                return redirect('parametres')
            else:
                data = {
                    'nrec': recruteur.objects.get(utilisateur=request.user),
                    'username':request.user.username
                }
                return render(request, 'recruteur/parametres.html', data)
        return redirect('index')
    else:
        return redirect('index')