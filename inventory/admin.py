from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, Profile

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)
admin.site.register(Profile)
