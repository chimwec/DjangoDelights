from django.urls import path, include
from . import views
from .views import PurchaseForm, Inventory, MenuItem, IngredientDelete, IngredientListView, Profit, Revenue

urlpatterns = [
    path('', views.home, name='home'),
    path('purchase_item/', views.PurchaseForm, name='purchase_item'),
    path('inventory/', views.Inventory.as_view(), name='Inventory'),
    path('ingredients/list/', IngredientListView.as_view(), name='ingredients-list'),
    path('ingredient/delete/', views.IngredientDelete.as_view(), name='ingredientDelete'),
    path('menu/list/', MenuItem.as_view(), name='MenuItem'),
    path('purchase/', views.Purchase.as_view(), name='purchase'),
    path('profit/', Profit.as_view(), name='profit'),
    path('revenue/', Revenue.as_view(), name='revenue'),
]