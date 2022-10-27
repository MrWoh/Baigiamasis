from django.urls import path
from .views import (
    ProductsListView,
    add_to_order,
    delete_from_order,
    order_details,
    EditOrderView,
    EditOrderItemView,
)

urlpatterns = [
    path('product_list/', ProductsListView.as_view(), name='product_list'),
    path('my_order/', order_details, name="my_order"),
    path('add_to_order/<int:item_id>/<int:supplier_id>',
         add_to_order, name="add_to_order"),
    path('edit_order_item/<int:pk>',
         EditOrderItemView.as_view(), name="edit_order_item"),
    path('edit_order/<int:pk>',
         EditOrderView.as_view(), name="edit_order"),
    path('remove_from_order/<int:item_id>',
         delete_from_order, name="remove_from_order"),
]
