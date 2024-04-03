# Generated by Django 4.0.4 on 2022-05-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruteur', '0020_alter_offre_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruteur',
            name='secteur',
            field=models.CharField(choices=[('Agence pub / Marketing Direct', 'Agence pub / Marketing Direct'), ('Agriculture / Environnement', 'Agriculture / Environnement'), ('Agroalimentaire', 'Agroalimentaire'), ('Ameublement / Décoration', 'Ameublement / Décoration'), ('Assurance / Courtage', 'Assurance / Courtage'), ('Audiovisuel', 'Audiovisuel'), ('Automobile / Motos / Cycles', 'Automobile / Motos / Cycles'), ('Autres Industries', 'Autres Industries'), ('Autres services', 'Autres services'), ('Aéronautique / Spatial', 'Aéronautique / Spatial'), ('BTP / Génie Civil', 'BTP / Génie Civil'), ('Banque / Finance', 'Banque / Finance'), ('Centre dappel', 'Centre dappel'), ('Chimie / Parachimie / Peintures', 'Chimie / Parachimie / Peintures'), ('Communication / Evénementiel', 'Communication / Evénementiel'), ('Comptabilité / Audit', 'Comptabilité / Audit'), ('Conseil / Etudes', 'Conseil / Etudes'), ('Cosmétique / Parfumerie / Luxe', 'Cosmétique / Parfumerie / Luxe'), ('Distribution', 'Distribution'), ('Edition / Imprimerie', 'Edition / Imprimerie'), ('Electricité', 'Electricité'), ('Electro-mécanique / Mécanique', 'Electro-mécanique / Mécanique'), ('Electronique', 'Electronique'), ('Energie', 'Energie'), ('Enseignement / Formation', 'Enseignement / Formation'), ('Extraction / Mines', 'Extraction / Mines'), ('Ferroviaire', 'Ferroviaire'), ('Hôtellerie / Restauration', 'Hôtellerie / Restauration'), ('Immobilier / Promoteur / Agence', 'Immobilier / Promoteur / Agence'), ('Import / Export / Négoce', 'Import / Export / Négoce'), ('Informatique', 'Informatique'), ('Internet / Multimédia', 'Internet / Multimédia'), ('Juridique / Cabinet d’avocats', 'Juridique / Cabinet d’avocats'), ('Matériel Médical', 'Matériel Médical'), ('Métallurgie / Sidérurgie', 'Métallurgie / Sidérurgie'), ('Nettoyage / Sécurité / Gardiennage', 'Nettoyage / Sécurité / Gardiennage'), ('Offshoring / Nearshoring', 'Offshoring / Nearshoring'), ('Papier / Carton', 'Papier / Carton'), ('Pharmacie / Santé', 'Pharmacie / Santé'), ('Plasturgie', 'Plasturgie'), ('Presse', 'Presse'), ('Pétrole / Gaz', 'Pétrole / Gaz'), ('Recrutement / Intérim', 'Recrutement / Intérim'), ('Service public / Administration', 'Service public / Administration'), ('Tabac', 'Tabac'), ('Telecom', 'Telecom'), ('Textile / Cuir', 'Textile / Cuir'), ('Tourisme / Voyage / Loisirs', 'Tourisme / Voyage / Loisirs'), ('Transport / Messagerie / Logistique', 'Transport / Messagerie / Logistique')], max_length=50, null=True),
        ),
    ]
