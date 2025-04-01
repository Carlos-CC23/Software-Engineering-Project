from django.shortcuts import render, get_object_or_404

from django.db.models import Q  # <-- Import Q for complex queries
from .models import Recipe

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_list(request):
    query = request.GET.get('query', '')
    medical_condition = request.GET.get('medical_condition', '')

    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) |   # Search by name
            Q(ingredients__icontains=query)  # Search by ingredients
        )
    if medical_condition:
        recipes = recipes.filter(medical_conditions__icontains=medical_condition)

    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
