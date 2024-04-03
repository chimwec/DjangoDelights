from django import forms
from.models import MenuItem, Ingredient, RecipeRequirement, Purchase


class PurchaseForm(forms.Form):
    menu_item = forms.ModelChoiceField(queryset=MenuItem.objects.all())
    quantity = forms.IntegerField(min_value=1)
    notes = forms.CharField(max_length=200, required=False)