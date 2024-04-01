from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import PurchaseForm  # Assuming you have a form for purchase details
from django.views import TemplateView
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')


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
                ...

                # Create purchase record
                purchase = Purchase.objects.create(
                    menu_item=menu_item,
                    # ... other purchase details
                )
                return redirect('purchase_success')  
            else:
                return render(request, 'purchase_failed.html') 
    else:
        # GET request - Display your form
        form = PurchaseForm()
        return render(request, 'purchase_form.html', {'form': form})


class InventoryView(TemplateView):
    template_name = 'inventory_app/inventory.html'  # Adjust template path

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