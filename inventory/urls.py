from django.urls import path, include
from . import views
from .views import PurchaseListView, MenuItemListView, IngredientDelete, IngredientListView, Profit, PurchaseItemView, RecipeRequirementListView
from.forms import PurchaseForm, IngredientForm, MenuItemForm

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('ingredients', IngredientListView.as_view(), name='ingredients-list'),
    path('ingredients/new/', views.IngredientCreate.as_view(), name='ingredient-create'),
    path('menu/', MenuItemListView.as_view(), name='menuitem'),
    path('menu/new/', views.MenuItemCreate.as_view(), name='menuitem-create'),
    path('purchase/', views.PurchaseListView.as_view(), name='purchase'),
    path('purchase/<int:menu_item_id>/', PurchaseItemView.as_view(), name='purchase_item'),
    path('purchaseform/', PurchaseForm, name='purchaseform'),
    path('purchase_item/', views.PurchaseForm, name='purchase_item'),
    path('reciperequirement', RecipeRequirementListView.as_view(), name='reciperequirement-list'),
    path('reciperequirement/new/', views.RecipeRequirementCreate.as_view(), name='reciperequirement-create'),
    path('profit_revenue/', Profit.as_view(), name='profit_revenue'),
]