from django.db import models

from authentification.models import User
# Create your models here.


class Recettes(models.Model):
    titre = models.CharField(max_length=60)
    description = models.CharField(max_length=400)
    ingredients = models.TextField(blank=True)
    etapes = models.TextField(blank=True)
    user = models.ForeignKey (User, on_delete=models.CASCADE) #Existe dans l'app authentification

class Notes(models.Model):
    valeur_notes = models.PositiveSmallIntegerField
    recettes = models.ForeignKey(Recettes, on_delete=models.CASCADE)
    user = models.ForeignKey (User, on_delete=models.CASCADE)


class Commentaires(models.Model):
    contenu_com = models.CharField(max_length=255)
    date_publication = models.DateTimeField(auto_now_add=True)
    recettes = models.ForeignKey(Recettes,on_delete=models.CASCADE)
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    



