from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Supplier, MySupplier

from .forms import AddSupplierForm


class SuppliersListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'suppliers.html'
    context_object_name = 'suppliers'


class MySuppliersView(LoginRequiredMixin, ListView):
    model = MySupplier
    template_name = 'my_suppliers.html'
    context_object_name = 'my_suppliers'

    def get_queryset(self):
        return MySupplier.objects.filter(user=self.request.user)


class AddSupplierView(LoginRequiredMixin, CreateView):
    form_class = AddSupplierForm
    model = MySupplier
    template_name = 'add_supplier.html'
    context_object_name = 'add_supplier'
    success_url = reverse_lazy('my_supplier_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditMySupplierView(LoginRequiredMixin, UpdateView):
    form_class = AddSupplierForm
    model = MySupplier
    template_name = 'edit_supplier.html'
    context_object_name = 'edit_supplier'
    success_url = reverse_lazy('my_supplier_list')
