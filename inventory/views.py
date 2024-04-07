from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import PurchaseForm  # Assuming you have a form for purchase details
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Sum
from django.views.generic.edit import DeleteView

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')



# this is a view that will show a list of ingredient
class IngredientList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'


# this view is for deleting ingredients
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'


# this view will show the menu items
class MenuItem(ListView):
    model = MenuItem
    template_name = 'inventory/menu_list.html'

# this view shows the purchses made 
class Purchase(DetailView):
    model = Purchase
    template_name = 'inventory/purchase.html'


# this view is to show profit
class Profit(TemplateView):
    template_name = 'inventory/profit.html'


# this view shows the revenue
class Revenue(TemplateView):
    template_name = 'inventory/revenue.html'


# this view is a purchase form 
def purchase_item(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            menu_item_id = form.cleaned_data['menu_item']
            menu_item = MenuItem.objects.get(id=menu_item_id)

            # Check inventory
            sufficient_inventory = True  # Placeholder - you'd implement inventory logic
            if sufficient_inventory:
                # Subtract quantities from inventory (loop through recipe requirements)
                for recipe_requirement in menu_item.recipe_requirements.all():
                    ingredient = recipe_requirement.ingredient
                    ingredient.available_quantity -= recipe_requirement.quantity
                    ingredient.save()
                ...

                # Create purchase record
                purchase = Purchase.objects.create(
                    menu_item=menu_item,
                    # ... other purchase details
                    quantity=form.cleaned_data['quantity'],
                    price=form.cleaned_data['quantity'] * menu_item.price,
                )
                return redirect('purchase_success')  
            else:
                return render(request, 'purchase_failed.html') 
    else:
        # GET request - Display your form
        form = PurchaseForm()
        return render(request, 'purchase_form.html', {'form': form})

# this view is showing the inventory
class InventoryView(TemplateView):
    template_name = 'inventory/inventory.html'  # Adjust template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_inventory'] = Ingredient.objects.all()
        context['purchases'] = Purchase.objects.all()
        context['menu'] = MenuItem.objects.all()
        context['total_purchases'] = Purchase.objects.aggregate(total_purchases=Sum('quantity'))['total_purchases']
        context['total_revenues'] = Purchase.objects.aggregate(total_revenues=Sum('menu_item__price_per_unit'))['total_revenues']
        context['total_costs'] = context['total_revenues'] - context['total_purchases']
        context['profit'] = context['total_revenues'] - context['total_costs']
        # ... other queries and calculations ...
        return context
    


