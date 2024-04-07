from django.urls import path, include
from . import views
from .views import PurchaseForm, InventoryView, MenuItem, IngredientDelete, IngredientList, Profit, Revenue

urlpatterns = [
    path('', views.home, name='home'),
    path('purchase_item/', views.PurchaseForm, name='purchase_item'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('ingredient/list/',views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/delete/',views.IngredientDelete.as_view(), name='ingredientDelete'),
    path('Menu/list/', MenuItem.as_view(), name='menulist'),
    path('purchase/', views.Purchase.as_view(), name='purchase'),
    path('profit/', Profit.as_view(), name='profit'),
    path('revenue/', Revenue.as_view(), name='revenue'),
]