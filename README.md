# Software-Engineering-Project
Creating a database for healthy recipes for the Public Health Department

Welcome to the Recipe and Patient Management Site!

This Django web application allows users to:
- Browse a database of healthy recipes.
- Filter recipes by name, ingredients, and medical conditions.
- Calculate recommended daily calories based on personal metrics.

For Admin-only features:
- Manage patient appointment histories and their track questionnaire responses.
- Add, Remove, and Modify recipes

---

## 🚀 Features

### Recipe Management
- View detailed recipes with ingredients, preparation steps, and nutritional information.
- Search recipes by name or ingredient.
- Filter recipes based on specific medical conditions (e.g., diabetes-friendly recipes).
- Pagination for browsing multiple recipes easily.

### Calorie Calculator
- Input gender, height, weight, age, activity level, and goals.
- Automatically calculates Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE), and suggested macronutrient distribution.

### Appointment History (Admin Only)
- Record patient appointment discussions.
- Fill out a pre-determined health questionnaire for each patient.
- Track appointment creation time and the admin who recorded it.

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Django 4+**
- **SQLite** (Default database for easy setup)
- **HTML/CSS/JavaScript** (basic front-end templates)
- **Django Admin** for backend management

---

## ⚙️ Installation

# How to run it:
Steps: 

1) Create a virtual environment in the terminal, paste this -> py -3 -m venv .venv
2) Then paste this -> .venv\scripts\activate
3) Type this to download Djanjo -> python -m pip install django
4) Then type this in to download Pillow -> python -m pip install Pillow
5) then type this download Django language -> pip install django-modeltranslation
6) Then type cd recipe_site_v6
7) Then type python manage.py runserver

-Use these links to accces the main website and the admin side

  -Admin : http://127.0.0.1:8000/admin/
  
  -Website: http://127.0.0.1:8000/recipes/

