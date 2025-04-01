from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    medical_conditions = models.TextField(blank=True, null=True)
    preparation_steps = models.TextField()
    nutritional_info = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)

class AppointmentHistory(models.Model):
    patient_name = models.CharField(max_length=100)
    discussion_notes = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.patient_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    #def __str__(self):
    #    return self.name
