from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import PurchaseForm, IngredientForm, MenuItemForm# Assuming you have a form for purchase details
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Sum
from django.views.generic.edit import DeleteView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class home(TemplateView):
   template_name = 'inventory/home.html'

   def get_context_data(self):
       context = super().get_context_data()
       context["ingredients"] = Ingredient.objects.all()
       context["menu"] = MenuItem.objects.all()
       context["purchase"] = Purchase.objects.all()
       return context

# this view is to show profit
class Profit(TemplateView):
    template_name = 'inventory/profit_revenue.html'


# all Listviews below
    
# this is a view that will show a list of ingredient
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredients-list.html'
    context_object_name = 'ingredients'

    def get_queryset(self):
        return Ingredient.objects.all()


# this view will show the menu items
class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'menu'


    def get_queryset(self):
        return MenuItem.objects.all()


# this view shows the purchses made 
class PurchaseListView(ListView):
    model = Purchase
    template_name = 'inventory/purchase.html'


# all createview below

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/'


class PurchaseCreate(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase_create.html'


class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredient_create.html'



  # decreasing ingredient.quantity because ingredients were used for the purchased menu_item.
    def form_valid(self, form):
      item = form.save(commit=False)
      menu_item = MenuItem.objects.get(id = item.menu_item.id)
      recipe_requirements  = RecipeRequirement.objects.filter(menu_item = menu_item)
      errors_list = []

      for requirement in recipe_requirements:
        ingredient = requirement.ingredient
        required_quantity = requirement.quantity


        if ingredient.quantity >= required_quantity:
            ingredient.quantity -= required_quantity
            ingredient.save()
        else:
            errors_list.append(ingredient.name)

      if not errors_list:
          item.save()
          messages.success(self.request, "Purchase successful!")
          return super().form_valid(form)
      else:
          error_string = ", ".join(errors_list)
          messages.error(self.request, f"Not enough ingredients in the inventory: {error_string}")
          return self.render_to_response(self.get_context_data(form=form))


    

# this view is for deleting ingredients
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
