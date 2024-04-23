from django.db import models
from django.utils import timezone

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
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def has_enough_inventory(self,quantity):
        return self.inventory >= quantity
        self.save()

    
    def subtract_from_inventory(self, quantity):
        if self.has_enough_inventory(quantity):
            self.inventory -= quantity
            self.save()
            

    def get_absolute_url(self):
        return "/menu"
       
    def __str__(self):
        return self.name



class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=200, choices=UNIT_CHOICES, default='')


    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return self.name
    

    
class RecipeRequirement(models.Model):
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return "/reciperequirement"

    def __str__(self):
        return self.ingredient.name
    


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)


    def get_absolute_url(self):
        return "/purchase"

    def __str__(self):
        return f"{self.menu_item} was purchased at {self.timestamp}"
    



