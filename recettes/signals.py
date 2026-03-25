from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Notes, Recettes
from django.db.models import Avg

@receiver(post_save, sender=Notes)
def update_moyenne_note(sender, instance, **kwargs):
    recette = instance.recettes
    moyenne = Notes.objects.filter(recettes=recette).aggregate(Avg('valeur_notes'))['valeur_notes__avg']
    recette.moyenne_notes = moyenne or 0
    recette.save()

@receiver(post_delete, sender=Notes)
def update_moyenne_note_delete(sender, instance, **kwargs):
    recette = instance.recettes
    moyenne = Notes.objects.filter(recettes=recette).aggregate(Avg('valeur_notes'))['valeur_notes__avg']
    recette.moyenne_notes = moyenne or 0
    recette.save()