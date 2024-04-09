from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase, Inventory
from .forms import PurchaseForm  # Assuming you have a form for purchase details
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Sum
from django.views.generic.edit import DeleteView

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')



# this is a view that will show a list of ingredient
class Ingredient(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient.html'
    context_object_name = 'data'


# this view is for deleting ingredients
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'


# this view will show the menu items
class MenuItem(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'data'



# this view shows the purchses made 
class Purchase(DetailView):
    model = Purchase
    template_name = 'inventory/purchase.html'
    get_context_data = 'data'


# this view is to show profit
class Profit(TemplateView):
    template_name = 'inventory/profit.html'


# this view shows the revenue
class Revenue(TemplateView):
    template_name = 'inventory/revenue.html'


# this view is showing the inventory
class Inventory(ListView):
    model = Inventory
    template_name = 'inventory/inventory.html'  # Adjust template path
    context_object_name = 'inventory'

    queryset = Inventory.objects.filter()
    


