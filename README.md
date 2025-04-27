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
- **SQLite** 
- **HTML/CSS/JavaScript** 
- **Django Admin** for backend management

---

## ⚙️ Installation

Steps: 

1) Create a virtual environment in the terminal, paste this -> py -3 -m venv .venv
2) Then paste this -> .venv\scripts\activate
3) Type this to download Djanjo -> python -m pip install django
4) Then type this in to download Pillow -> python -m pip install Pillow
5) then type this download Django language -> pip install django-modeltranslation
6) Then type cd recipe_site_v6
7) Then type python manage.py runserver

## 🔒 Website & Admin Access

-Use these links to accces the main website and the admin side

  -Admin : http://127.0.0.1:8000/admin/
  
  -Website: http://127.0.0.1:8000/recipes/

## 📂 Project Structure Overview

recipe_site_v6/
├── recipes/                  # Main Django app
│   ├── models.py              # Recipe and Appointment models
│   ├── views.py               # Recipe views and calorie calculator
│   ├── templates/             # HTML templates
│   ├── static/                # CSS, JS, and image files
│   └── admin.py               # Admin panel customizations
├── recipe_site/               # Project settings and URLs
├── db.sqlite3                 # Default database
├── manage.py                  # Django management file


## 📜 License
This project is for educational purposes and is not intended for commercial use.

## ✨ Acknowledgments
Special thanks to the tutorials and Django documentation that helped during development.





