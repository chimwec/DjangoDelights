from django import forms
from.models import MenuItem, Ingredient, RecipeRequirement, Purchase, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PurchaseForm(forms.ModelForm):
    class Meta:
      model = Purchase
      fields = "__all__"

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
      
class ProfileForm(forms.ModelForm):
   class Meta:
      model = Profile
      fields = "__all__"

class LoginViewForm(forms.ModelForm):
   class Meta:
      fields = "__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
        ]
