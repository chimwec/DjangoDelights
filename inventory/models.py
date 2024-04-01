from django.db import models


# Create your models here.


class MenuItem(models.Model):
    """
    MenuItem model represents a menu item with a name, description, and price.
    
    Fields:
    
      name (CharField): Name of the menu item.
    
      description (TextField): Description of the menu item. 
    
      price (DecimalField): Price of the menu item.
    
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return self.name



class Ingredient(models.Model):
    """
    Ingredient model representing an ingredient that the restaurant has in its inventory.
    
    Attributes:
      - name (str): Name of the ingredient
      - available_quantity (Decimal): Available quantity in stock
      - price_per_unit (Decimal): Cost per unit of the ingredient
      - unit (str): Unit of measurement for the ingredient (e.g. grams) 
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    available_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=200, default='units')

    def __str__(self):
        return self.name
    
    
    
    
class RecipeRequirement(models.Model):
    # represents a single ingredient and how much of it is required for an item off the menu
    # Models a requirement for a recipe (menu item). Links the menu item to the 
    # required ingredient and quantity. Also links to the recipe itself as a ))
    # foreign key to confirm the recipe.
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.ingredient.name
    

    

class Purchase(models.Model):
    """Records a purchase of a menu item.
    
    Attributes:
        menu_item (MenuItem): The purchased menu item.
        quantity (Decimal): The quantity purchased.
        price (Decimal): The total price paid.
        timestamp (DateTime): When the purchase occurred.
    
    """
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.menu_item.name} - Quantity: {self.quantity}, Price: {self.price}, Timestamp: {self.timestamp}"