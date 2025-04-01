from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    medical_conditions = models.TextField(blank=True, null=True)
    preparation_steps = models.TextField()
    nutritional_info = models.TextField(blank=True, null=True)  # New Field
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)  # Ensure blank=True, null=True for optional images

    def __str__(self):
        return self.name
