from functools import wraps
from django.shortcuts import get_object_or_404, redirect

from .models import Recettes
def one_rating_only(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        id = kwargs.get('recette_id')
        recette = get_object_or_404(Recettes, id=id)
        notes = recette.notes_set.all()
        note_limite = notes.filter(user=request.user)
        if note_limite:
           return redirect("home_page")
        return view_func(request, *args, **kwargs)
    return _wrapped  
        