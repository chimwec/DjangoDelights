from django.urls import path, include
from . import views
from .views import PurchaseForm

urlpatterns = [
    path('', views.home, name='home'),
    path('purchase_item/', views.PurchaseForm, name='purchase_item'),
]