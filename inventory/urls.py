from django.urls import path, include
from . import views
from .views import PurchaseCreate, MenuItemListView, IngredientDelete, IngredientListView, Profit, RecipeRequirementListView, PurchaseListView
from.forms import PurchaseForm, IngredientForm, MenuItemForm

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('ingredients/list', IngredientListView.as_view(), name='ingredients-list'),
    path('ingredients/new/', views.IngredientCreate.as_view(), name='ingredient-create'),
    path('menu/', MenuItemListView.as_view(), name='menuitem'),
    path('menu/new/', views.MenuItemCreate.as_view(), name='menuitem-create'),
    path('purchase/list', PurchaseListView.as_view(), name='purchase-list'),
    path('purchase/', PurchaseCreate.as_view(), name='purchase_create'),
    path('reciperequirement', RecipeRequirementListView.as_view(), name='reciperequirement-list'),
    path('reciperequirement/new/', views.RecipeRequirementCreate.as_view(), name='reciperequirement-create'),
    path('profit_revenue/', Profit.as_view(), name='profit_revenue'),
]