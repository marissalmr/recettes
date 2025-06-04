from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


from authentification.models import User
# Create your models here.


class Recettes(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_title = models.CharField(max_length=60)
    short_description = models.CharField(max_length=400)
    ingredients_list = models.TextField(blank=True)
    preparation_steps = models.TextField(blank=True) 
    category_choices= [
        ("appetizers", "Appetizers"),
        ("main dishes", "Main Dishes"),
        ("soups", "Soups"),
        ("salads", "Salads"),
        ("desserts", "Desserts")
        
    ]

    category_choices = models.CharField(default="", choices=category_choices, max_length=60)
    time_in_minutes = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    user = models.ForeignKey (User, on_delete=models.CASCADE) 


class Notes(models.Model):
    valeur_notes = models.PositiveSmallIntegerField(default=0)
    recettes = models.ForeignKey(Recettes, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



class Commentaires(models.Model):
    contenu_com = models.CharField(max_length=255)
    date_publication = models.DateTimeField(auto_now_add=True)
    recettes = models.ForeignKey(Recettes,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    




