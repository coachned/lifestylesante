# Generated by Django 5.1.4 on 2025-03-04 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RapportMensuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.IntegerField()),
                ('annee', models.IntegerField()),
                ('total_arrivees', models.IntegerField(default=0, verbose_name='Arrivées signalées')),
                ('total_departs', models.IntegerField(default=0, verbose_name='Départs signalés')),
                ('total_montant', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Gain mensuel')),
                ('employe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.employe')),
            ],
            options={
                'unique_together': {('employe', 'mois', 'annee')},
            },
        ),
    ]
