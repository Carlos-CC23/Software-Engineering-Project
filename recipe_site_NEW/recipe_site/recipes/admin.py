from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'medical_conditions', 'nutritional_info', 'image')

admin.site.register(Recipe, RecipeAdmin)
