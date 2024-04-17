from django import forms
from.models import MenuItem, Ingredient, RecipeRequirement, Purchase


class PurchaseForm(forms.Form):
    class Meta:
       model = Purchase
       fields = ['menu_item', 'quantity', 'notes']

class IngredientForm(forms.Form):
    class Mete:
      Ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all())
      quantity = forms.IntegerField(min_value=1)
      notes = forms.CharField(max_length=200, required=False)


class MenuItemForm(forms.Form):
    class Meta:
      MenuItem = forms.ModelChoiceField(queryset=MenuItem.objects.all())
