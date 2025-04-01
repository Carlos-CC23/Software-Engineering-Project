from django.contrib import admin
from .models import Recipe
from .models import Recipe, AppointmentHistory  # Make sure to import AppointmentHistory

#admin.site.register(Recipe, RecipeAdmin)

@admin.register(AppointmentHistory)
class AppointmentHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'created_at')
    search_fields = ('patient_name',)
    ordering = ('-created_at',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'medical_conditions', 'nutritional_info', 'image')

admin.site.register(Recipe)
