from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from inventory.models import MenuItem, Ingredient, Purchase, RecipeRequirement
from inventory.forms import PurchaseForm
from inventory.views import PurchaseCreate
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.core.exceptions import ValidationError  # Import for raising validation errors
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangodelights.settings")


# Create your tests here.
class MenuItemViewTest(TestCase):
    def setUp(self):
        # Create some sample menu items for testing
        self.item1 = MenuItem.objects.create(name='Item 1', description='Description 1', price=10.00)
        self.item2 = MenuItem.objects.create(name='Item 2', description='Description 2', price=15.00)

    def test_menu_item_view_status_code(self):
        # Get the URL for the MenuItemView
        url = reverse('menuitem')
        
        # Use the client to make a GET request to the view
        response = self.client.get(url)
        
        # Check that the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

    def test_menu_item_view_template(self):
        # Get the URL for the MenuItemView
        url = reverse('menuitem')
        
        # Use the client to make a GET request to the view
        response = self.client.get(url)
        
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'inventory/menu.html')

    def test_menu_item_view_context(self):
        # Get the URL for the MenuItemView
        url = reverse('menuitem')
        
        # Use the client to make a GET request to the view
        response = self.client.get(url)
        
        # Check that the context contains the menu items
        self.assertIn('menu', response.context)
        self.assertEqual(list(response.context['menu']), [self.item1, self.item2])



class PurchaseCreateTest(TestCase):

    def setUp(self):
        # Create some test data
        menu_item = MenuItem.objects.create(name="Test_MenuItem")
        ingredient1 = Ingredient.objects.create(name="Ingredient 1", quantity=2)
        ingredient2 = Ingredient.objects.create(name="Ingredient 2", quantity=1)
        RecipeRequirement.objects.create(menu_item=menu_item, ingredient=ingredient1, quantity=2)
        RecipeRequirement.objects.create(menu_item=menu_item, ingredient=ingredient2, quantity=3)

    def test_sufficient_quantity(self):
        # Purchase with sufficient quantity
        data = {"menu_item": self.menu_item.id}
        form = PurchaseForm(data=data)
        self.assertTrue(form.is_valid())

        with self.assertLogs('purchase', level='INFO') as cm:
            form.save()

        self.assertEqual(len(cm.output), 1)
        self.assertIn("success message added", cm.output[0])

        # Check ingredient quantities after purchase
        ingredient1 = Ingredient.objects.get(name="Ingredient 1")
        ingredient2 = Ingredient.objects.get(name="Ingredient 2")
        self.assertEqual(ingredient1.quantity, 8)
        self.assertEqual(ingredient2.quantity, 2)

    def test_insufficient_quantity(self):
        # Purchase with insufficient quantity for Ingredient 1
        data = {"menu_item": self.menu_item.id}
        form = PurchaseForm(data=data)
        self.assertTrue(form.is_valid())

        ingredient1.quantity = 1  # Modify quantity to be insufficient

        with self.assertRaises(ValidationError):
            form.save()

        # Check ingredient quantities remain unchanged
        ingredient1 = Ingredient.objects.get(name="Ingredient 1")
        ingredient2 = Ingredient.objects.get(name="Ingredient 2")
        self.assertEqual(ingredient1.quantity, 1)
        self.assertEqual(ingredient2.quantity, 5)

        with self.assertLogs('purchase', level='ERROR') as cm:
            self.assertRaises(ValidationError, form.save)

        self.assertEqual(len(cm.output), 1)
        self.assertIn("Error message added: Ingredient 1", cm.output[0])

