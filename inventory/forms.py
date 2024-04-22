from django import forms
from.models import MenuItem, Ingredient, RecipeRequirement, Purchase


class PurchaseForm(forms.Form):
    class Meta:
       model = Purchase
       fields = ['menu_item', 'quantity', 'notes']

class IngredientForm(forms.ModelForm):
    class Meta:
      model = Ingredient
      fields = "__all__"

class MenuItemForm(forms.ModelForm):
    class Meta:
      model = MenuItem
      fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
   class Meta:
      model = RecipeRequirement 
      fields = "__all__"