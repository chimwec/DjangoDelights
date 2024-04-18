from typing import Any
from datetime import datetime
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import PurchaseForm, IngredientForm, MenuItemForm# Assuming you have a form for purchase details
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Sum
from django.views.generic.edit import DeleteView, CreateView, View
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

# this view gets the purchase and then subtract the inventory
class PurchaseItemView(View):
    def post(self, request, menu_item_id):
        # Retrieve the selected menu item
        menu_item = MenuItem.objects.get(pk=menu_item_id)

        # Assuming a form is submitted with quantity data
        quantity = request.POST.get('quantity', 1)  # Default to 1 if not provided

        # Check if there are enough ingredients in inventory
        if menu_item.has_enough_inventory(int(quantity)):
            # Record the purchase
            purchase = Purchase.objects.create(
                menu_item=menu_item,
                quantity=quantity,
                purchase_timestamp=datetime.now()
            )

            # Update inventory by subtracting required ingredients
            menu_item.subtract_from_inventory(int(quantity))

            # Redirect to a success page or display a success message
            return redirect('purchase_success')

        else:
            # Display error message - insufficient ingredients
            return render(request, 'purchase_error.html', {'error_message': 'Insufficient ingredients'})




# all createview below

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/add_menu.html'


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
        return super(self).form_valid(form)
    else:
          error_string = ", ".join(errors_list)
          messages.error(self.request, f"Not enough ingredients in the inventory: {error_string}")
          return self.render_to_response(self.get_context_data(form=form))


# view the profit and revenue for the restaurant.
def profit_revenue(request):
    context = {}
    context["menu"] = MenuItem.objects.all()
    context["purchase"] = Purchase.objects.all()
    context["profit"] = Purchase.objects.all().aggregate(Sum('menu_item__price'))
    context["revenue"] = Purchase.objects.all().aggregate(Sum('menu_item__price'))
    return render(request, 'inventory/profit_revenue.html', context)

    

# this view is for deleting ingredients
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
