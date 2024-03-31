from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import PurchaseForm  # Assuming you have a form for purchase details

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
