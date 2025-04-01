from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q  
from .models import Recipe
from django.shortcuts import render, redirect #for the appointments
from .forms import AppointmentHistoryForm #importing the forms.py 
from .models import AppointmentHistory 

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_list(request):
    query = request.GET.get('query', '')
    medical_condition = request.GET.get('medical_condition', '')

    recipes = Recipe.objects.all()

    all_conditions = Recipe.objects.exclude(medical_conditions="").values_list('medical_conditions', flat=True)
    unique_conditions = sorted(set(all_conditions))

    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) |   
            Q(ingredients__icontains=query) 
        )

    if medical_condition:
        recipes = recipes.filter(medical_conditions__icontains=medical_condition)

    paginator = Paginator(recipes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/recipe_list.html', {
        'page_obj': page_obj,
        'medical_conditions': unique_conditions
    })

def add_appointment_history(request):
    if request.method == 'POST':
        form = AppointmentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('history_list')
    else:
        form = AppointmentHistoryForm()
    
    return render(request, 'recipes/add_history.html', {'form': form})

def history_list(request):
    histories = AppointmentHistory.objects.all().order_by('-created_at')
    return render(request, 'recipes/history_list.html', {'histories': histories})
