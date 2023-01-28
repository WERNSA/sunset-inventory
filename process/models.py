import uuid
from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

# Create your models here.
class Inventory(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)

    product = models.ForeignKey(Product, verbose_name='Producto', on_delete=models.RESTRICT, null=False, blank=False)
    quantity = models.DecimalField(verbose_name='Cantidad', decimal_places=2, max_digits=8, null=False, blank=False)
    buy_price = models.DecimalField(verbose_name='Precio de Compra', decimal_places=2, max_digits=8, null=False, blank=False)
    sell_price = models.DecimalField(verbose_name='Precio de Venta', decimal_places=2, max_digits=8, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='inventory_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='inventory_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} Cantidad:{}'.format(self.product, self.quantity)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'