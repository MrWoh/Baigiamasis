from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, UpdateView

from .forms import EditOrderForm, EditOrderItemForm

from .models import Products, OrderItem, Order
from supplier_manager.models import Supplier
from user_profile.models import Profile


class ProductsListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = 'product_list.html'
    context_object_name = 'products'
    success_url = reverse_lazy('my_supplier_list')

    def get_queryset(self):
        supplier_id = self.request.GET.get('supplier_id')
        supplier = Supplier.objects.get(pk=supplier_id)
        queryset = Products.objects.filter(supplier=supplier)
        return queryset


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(
        owner=user_profile, is_added=False)
    if order.exists():
        return order[0]
    return 0


@login_required()
def add_to_order(request, item_id, supplier_id):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = get_object_or_404(Products, id=item_id)
    supplier = get_object_or_404(Supplier, id=supplier_id)
    user_order, status = Order.objects.get_or_create(
        owner=user_profile, is_added=False, supplier=supplier)
    order_item, status = OrderItem.objects.get_or_create(
        product=product, order=user_order, supplier=supplier)
    if status:
        user_order.order_name = f'{user_profile.user}.{supplier.name} Order .{user_order.id}'
        user_order.save()

    messages.info(request, "Product added to order")
    return redirect(reverse('my_supplier_list'))


@login_required()
def delete_from_order(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('my_order'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'my_order.html', context)


class EditOrderItemView(LoginRequiredMixin, UpdateView):
    form_class = EditOrderItemForm
    model = OrderItem
    template_name = 'edit_order_item.html'
    context_object_name = 'items'
    success_url = reverse_lazy('my_order')


class EditOrderView(LoginRequiredMixin, UpdateView):
    form_class = EditOrderForm
    model = Order
    template_name = 'edit_order.html'
    context_object_name = 'items'
    success_url = reverse_lazy('my_order')
