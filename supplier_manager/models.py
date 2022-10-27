from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


def default_mail():
    return 'supplier@mail.com'


def default_number():
    return '+3706'


class Supplier(models.Model):
    name = models.CharField(
        _('Supplier'),
        max_length=25,
    )
    description = models.TextField(_('Description'),
                                   max_length=500,
                                   blank=True, null=True,
                                   )

    def get_absolute_url(self):
        return reverse('supplier', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')


class MySupplier(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True,
        related_name="supplier_user",
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE, null=True,
        related_name="my_supplier",
    )
    email = models.EmailField(
        _('Email'),
        max_length=50,
        default=default_mail,
    )
    phone = models.CharField(
        _('Phone Number'),
        max_length=20,
        default=default_number,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.user, self.supplier.name)

    class Meta:
        verbose_name = _('My Supplier')
