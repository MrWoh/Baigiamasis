from django.contrib import admin

from .models import Products, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'unit', 'order_code', 'price',)


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
