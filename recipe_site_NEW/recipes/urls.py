from django.urls import path
from .views import recipe_list, recipe_detail
from . import views # for the appointments add and list

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('appointments/add/', views.add_appointment_history, name='add_history'),
    path('appointments/list/', views.history_list, name='history_list'),
]
