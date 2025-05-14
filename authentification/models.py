from django.db import models  
from django.contrib.auth.models import AbstractUser 
from django.core.validators import MaxValueValidator, MinValueValidator 



class User(AbstractUser): #Classe contenant tous les champs du User par défaut
    niveau= [
        ("débutant","Débutant"), #Le premier c'est ce qui est stocké  dans la base, le deuxième c'est ce qui est affiché à l'écran
        ("intérmediaire",'Intérmediaire'),
        ("professionnel","Professionnel")
    ]
    niveau_choix = models.CharField(default="Débutant", choices=niveau, max_length=100) #Obligé de faire ça pour stocker le niveau dans la BDD
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)]) #N'accepte pas de nombre négatifs, entre 1 et 100 pour controler l'entrée 

