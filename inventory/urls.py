from django.urls import path, include
from . import views
from django.conf import settings
from .views import logout_request


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('ingredient/List', views.IngredientsList.as_view(), name='ingredientslist'),
    path('ingredients/new/', views.IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredient/<pk>/update', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('ingredient/<pk>', views.IngredientDetail.as_view(), name='ingredientdetail'),
    path('ingredient/<pk>/delete/', views.IngredientDelete.as_view(), name='ingredientdelete'),
    path('menu/', views.MenuItemView.as_view(), name='menuitem'),
    path('menu/new/', views.MenuItemCreate.as_view(), name='menuitem-create'),
    path('menu/<pk>', views.MenuItemDetail.as_view(), name='menuitemdetail'),
    path('menu/<pk>/delete', views.MenuItemDelete.as_view(), name='menuitem_delete'),
    path('purchase/List', views.PurchaseList.as_view(), name='purchase-list'),
    path('purchase/', views.PurchaseCreate.as_view(), name='purchase_create'),
    path('reciperequirement/create', views.RecipeRequirementCreate.as_view(), name='reciperequirement_create'),
    path('profit_revenue/', views.profit_revenue, name='profit_revenue'),
    path('accounts/profile/', views.ProfileCreate.as_view(), name='profile'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', logout_request, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns