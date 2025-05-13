from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator 



class User(AbstractUser):
    niveau= [
        ("débutant","Débutant"),
        ("intérmediaire",'Intérmediaire'),
        ("Professionnel","Professionnel")
    ]
    niveau_choix = models.CharField(default="Débutant", choices=niveau, max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
