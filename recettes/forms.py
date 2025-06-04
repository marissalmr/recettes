from django.forms import ModelForm
from .models import Recettes, Notes, Commentaires  

class Creation(ModelForm):
    class Meta :
        model = Recettes
        fields = ["recipe_title", "short_description", "ingredients_list", "preparation_steps", "category_choices", 'time_in_minutes']

class Comments(ModelForm):
    class Meta :
        model = Commentaires
        fields = ["contenu_com"]





























