from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(default=False, verbose_name=_('is paid'))

    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    phone_number = models.CharField(max_length=15, verbose_name="_(Phone) Number")
    address = models.CharField(max_length=700, verbose_name=_("Address"))

    order_notes = models.CharField(max_length=700, blank=True, verbose_name=_("Order Notes"))

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_("Order"))
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items',
                                verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))
    price = models.PositiveIntegerField(verbose_name=_("Price"))

    def __str__(self):
        return f'Order Item {self.id}: {self.product} X {self.quantity} ({self.price}) '
