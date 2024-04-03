# Generated by Django 4.0.4 on 2022-05-05 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruteur', '0016_alter_recruteur_secteur'),
        ('demandeur', '0003_remove_demande_dem_remove_demande_ofr'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='dem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='demande',
            name='ofr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruteur.offre'),
        ),
    ]
