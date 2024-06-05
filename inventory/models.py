from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


UNIT_CHOICES = [
  ("g", "gram"),
  ("tbsp", "tablespoon"),
  ("tsp", "teaspoon"),
  ("l", "liter"),
  ("cup", "cup"),
  ("oz", "ounces"),
  ("lbs", "pound"),
  ("", "")
]

# Create your models here.


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def get_absolute_url(self):
        return "/menu"
       
    def __str__(self):
        return f"{self.name}, price: {self.price}"



class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=200, choices=UNIT_CHOICES, default='')


    def get_absolute_url(self):
        return "/ingredient"

    def __str__(self):
        return f"{self.name}: {self.price_per_unit} {self.unit}"
    


# represents a single ingredient and how much of it is required for an item on the menu
class RecipeRequirement(models.Model):
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    unit = models.CharField(max_length=200, choices=UNIT_CHOICES, default='')
   
    def get_absolute_url(self):
        return f"menu item: {self.menu_item}, ingredient: {self.ingredient}"

    def __str__(self):
        return  "/menu"
    


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)


    def get_absolute_url(self):
        return "/purchase"

    def __str__(self):
        return f"{self.menu_item} was purchased at {self.timestamp}"
    
#i have to make a migration first
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    # add more fields here
    #...
    
    def get_absolute_url(self):
        return "/profile"



