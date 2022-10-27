from django import forms

from .models import OrderItem, Order


class EditOrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('quantity',)


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('date_delivery', 'order_name',)
