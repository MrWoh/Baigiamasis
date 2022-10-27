from django.shortcuts import render
from django.contrib import messages
import openpyxl
from order_manager.models import Products
from tablib import Dataset
from .resources import ProductResources


def excel_upload(request):
    if request.method == 'POST':
        person_resource = ProductResources()
        dataset = Dataset()
        new_products = request.FILES['myfile']
        imported_data = dataset.load(new_products.read(), format='xlsx')
        for data in imported_data:
            value = Products(
                product_name=data[1],
                unit=data[2],
                order_code=data[3],
                price=data[4],
                supplier_id=data[5],
            )
            value.save()
        messages.info(request, "Product upload was successful")
    return render(request, 'excel_upload.html',)
