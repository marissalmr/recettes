from django.forms import ModelForm
from .models import Recettes, Notes, Commentaires  

class Creation(ModelForm):
    class Meta :
        model = Recettes
        fields = ["titre", "description", "ingredients", "etapes"]






















