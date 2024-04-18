from django.urls import path, include
from . import views
from .views import PurchaseListView, MenuItemListView, IngredientDelete, IngredientListView, Profit, PurchaseItemView
from.forms import PurchaseForm, IngredientForm, MenuItemForm

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('purchase_item/', views.PurchaseForm, name='purchase_item'),
    path('ingredients', IngredientListView.as_view(), name='ingredients-list'),
    path('ingredients/new/', views.IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredient/delete/', views.IngredientDelete.as_view(), name='ingredientDelete'),
    path('menu/', MenuItemListView.as_view(), name='menuitem'),
    path('menu/new/', views.MenuItemCreate.as_view(), name='menuitem-create'),
    path('purchase/', views.PurchaseListView.as_view(), name='purchase'),
    path('profit_revenue/', Profit.as_view(), name='profit_revenue'),
    path('purchase/<int:menu_item_id>/', PurchaseItemView.as_view(), name='purchase_item'),
    path('purchaseform/', PurchaseForm, name='purchaseform'),
]