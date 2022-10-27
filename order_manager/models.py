from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import datetime

from user_profile.models import Profile
from supplier_manager.models import Supplier


class Products(models.Model):
    UNIT_CHOICE = (
        ('a', _('Units')),
        ('b', _('Kg')),
        ('c', _('G')),
        ('d', _('L')),
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="product_supplier",
    )
    product_name = models.CharField(
        'Product name',
        max_length=50,
        default='Product'
    )
    unit = models.CharField(
        'Unit',
        max_length=1,
        choices=UNIT_CHOICE,
        default='a',
    )
    order_code = models.CharField(
        'Code',
        blank=True, null=True,
        max_length=20
    )
    price = models.DecimalField(
        'Price', default=0, max_digits=5, decimal_places=2,
    )

    def __str__(self):
        return '{}.  {}   {} {}'.format(self.product_name,
                                        self.get_unit_display(),
                                        self.order_code,
                                        self.price,
                                        )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class OrderItem(models.Model):
    product = models.OneToOneField(
        Products, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True)
    is_added = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="items")
    quantity = models.DecimalField(
        'Quantity', default=0, max_digits=6, decimal_places=2,
    )

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return '{}.'.format(self.product.product_name)


class Order(models.Model):
    order_name = models.CharField(max_length=25)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True)
    is_added = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    date_delivery = models.DateTimeField(
        "Delivery Date", default=datetime.today())

    def get_order_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.get_total for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.order_name)
