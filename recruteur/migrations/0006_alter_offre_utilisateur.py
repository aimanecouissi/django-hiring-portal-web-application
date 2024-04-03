# Generated by Django 4.0.4 on 2022-05-04 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruteur', '0005_alter_offre_options_offre_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offres', to=settings.AUTH_USER_MODEL),
        ),
    ]
