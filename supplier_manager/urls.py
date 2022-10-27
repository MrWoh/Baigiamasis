from django.urls import path
from .views import (
    SuppliersListView,
    MySuppliersView,
    AddSupplierView,
    EditMySupplierView,
)

urlpatterns = [
    path('suppliers/', SuppliersListView.as_view(), name='suppliers'),
    path('my_suppliers/', MySuppliersView.as_view(), name='my_supplier_list'),
    path('my_suppliers/<int:pk>/edit_supplier/',
         EditMySupplierView.as_view(), name='edit_supplier'),
    path('suppliers/add_supplier/',
         AddSupplierView.as_view(), name='add_supplier'),
]
