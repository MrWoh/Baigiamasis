from django import forms

from .models import MySupplier


class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = MySupplier
        fields = ('supplier', 'email', 'phone')
