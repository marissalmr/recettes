from django.urls import path

from recettes import views


urlpatterns = [
    path('homepage/',views.home_page, name='home_page'),
    path('create_recipes/', views.create_recipes, name = 'create_recipes'),
    path('recipes_details/<id>/', views.recipe_details, name="recipes_details"),
    path('update_recipes/<id_from_url>/', views.recipe_update, name='update_recipes'),
    path('my_recipes/', views.my_recipes, name="my_recipes"),
    path('delete_recipes/<id_from_url>/', views.recipe_delete, name="delete_recipes"),
    path('add_comments/<recette_id>/', views.add_comments, name='add_comments'),
    path('rating/<recette_id>/', views.rating, name='rating')


]