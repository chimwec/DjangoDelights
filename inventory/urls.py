from django.urls import path, include
from . import views
from .views import PurchaseListView, MenuItemListView, IngredientDelete, IngredientListView, Profit

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('purchase_item/', views.PurchaseForm, name='purchase_item'),
    path('ingredients/list/', IngredientListView.as_view(), name='ingredients-list'),
    path('ingredient/delete/', views.IngredientDelete.as_view(), name='ingredientDelete'),
    path('menu/list/', MenuItemListView.as_view(), name='menuitem'),
    path('purchase/', views.PurchaseListView.as_view(), name='purchase'),
    path('profit_revenue/', Profit.as_view(), name='profit_revenue'),
]