# Generated by Django 4.2.16 on 2024-10-01 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule_employe', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='employe_photos/')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('fonction', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MarquerArrivee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivee', models.BooleanField(default=True)),
                ('date_arrivee', models.DateTimeField(auto_now_add=True)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.employe')),
            ],
        ),
        migrations.CreateModel(
            name='MarquerDepart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.BooleanField(default=True)),
                ('date_depart', models.DateTimeField(auto_now_add=True)),
                ('date_arrivee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.marquerarrivee')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.employe')),
            ],
        ),
    ]
