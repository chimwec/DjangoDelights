from typing import Any
from datetime import datetime
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import PurchaseForm, IngredientForm, MenuItemForm, RecipeRequirementForm # Assuming you have a form for purchase details
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Sum
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.db import transaction


# Create your views here.
class home(TemplateView):
   template_name = 'inventory/home.html'

   def get_context_data(self):
       context = super().get_context_data()
       context["ingredients"] = Ingredient.objects.all()
       context["menu"] = MenuItem.objects.all()
       context["purchase"] = Purchase.objects.all()
       context["reciperequirement"] = RecipeRequirement.objects.all()
       return context
   
   
   # inventory/views.py


# this view is to show profit
class Profit(TemplateView):
    template_name = 'inventory/profit_revenue.html'




# all Listviews below   
    
# this is a view that will show a list of ingredient
class IngredientsList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredients-list.html'
    context_object_name = 'ingredients'

    def get_queryset(self):
        return Ingredient.objects.all()


# this view will show the menu items
class MenuItemView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'menu'


    def get_queryset(self):
        return MenuItem.objects.all()
    

class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement-list.html'
    context_object_name = 'reciperequirement'
    

    def get_queryset(self):
        return RecipeRequirement.objects.all()
    

# this view shows the purchses made 
class PurchaseList(ListView):
    model = Purchase
    template_name = 'inventory/purchase-list.html'
    context_object_name = 'purchases'
 



# all createview below

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menu_create.html'


class PurchaseCreate(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase_create.html'
    success_url = reverse_lazy('purchase-list')


class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredient_create.html'
    success_url = reverse_lazy('ingredientslist')


class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'inventory/reciperequirement_create.html'


#All Updateview
    
class IngredientUpdate(UpdateView):
  model = Ingredient
  template_name = "inventory/ingredient_update_form.html"
  form_class = IngredientForm
  success_url = reverse_lazy('ingredientslist')



#All Deleteview
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
    success_url = reverse_lazy('ingredientslist')



class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = 'inventory/menuitem_delete_form.html'
    success_url = reverse_lazy ('menuitem')




  # decreasing ingredient.quantity because ingredients were used for the purchased menu_item, have to finish the automatic subtractions in the inventory ingredients
    
def form_valid(self, form):
    item = form.save(commit=False)
    menu_item = MenuItem.objects.get(id = item.menu_item.id)
    recipe_requirements  = RecipeRequirement.objects.filter(menu_item = menu_item)
    errors_list = []

    ingredient_quantity_changes = {}
    for requirement in recipe_requirements:
        ingredient = requirement.ingredient
        required_quantity = requirement.quantity
        if ingredient.name in ingredient_quantity_changes:
            ingredient_quantity_changes[ingredient.name] += required_quantity
        else:
            ingredient_quantity_changes[ingredient.name] = required_quantity

    with transaction.atomic():
        for ingredient_name, quantity_change in ingredient_quantity_changes.items():
            ingredient = Ingredient.objects.get(name=ingredient_name)
            if ingredient.quantity < quantity_change:
               errors_list.append(ingredient_name)
            else:
               ingredient.quantity -= quantity_change
               ingredient.save()

    if not errors_list:
        item.save()
        messages.success(self.request, "Purchase successful!")
        print("success message added")
        return super(self).form_valid(form)
    else:
          error_string = ", ".join(errors_list)
          messages.error(self.request, f"Not enough ingredients in the inventory: {error_string}")
          print("Error message added:", error_string)
          return render(self.get_context_data(form=form)) #changed this from self.render_to_response
    



# view the profit and revenue for the restaurant.
def profit_revenue(request):
    context = {}
    context["menu"] = MenuItem.objects.all()
    context["purchase"] = Purchase.objects.all()
    context["profit"] = Purchase.objects.all().aggregate(Sum('menu_item__price'))
    context["revenue"] = Purchase.objects.all().aggregate(Sum('menu_item__price'))
    return render(request, 'inventory/profit_revenue.html', context)




class IngredientDetail(DetailView):
    model = Ingredient
    template_name = "inventory/ingredient_details.html"
    
    def get_context_data(self, **kwargs):
        context = super(IngredientDetail,self).get_context_data(**kwargs)
        context['object'] = self.object
        ingredient = Ingredient.objects.get(id=context['object'].pk)
        recipe_requirements_list = []
        for item in context['object'].reciperequirement_set.all():
            recipe_requirements_list.append(item)
        context = {
           'ingredient':ingredient,
           'recipe_requirements_list': recipe_requirements_list
        }
        return context



