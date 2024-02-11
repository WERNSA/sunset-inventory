import uuid
from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product
from django.contrib import admin

# Create your models here.
class Inventory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    product = models.ForeignKey(Product, verbose_name='Producto', on_delete=models.RESTRICT, null=False, blank=False)
    quantity = models.DecimalField(verbose_name='Cantidad', decimal_places=2, max_digits=8, null=False, blank=False)
    profit_unit = models.DecimalField(verbose_name='Ganancia Por Unidad C$', decimal_places=2, max_digits=8, null=False, blank=False)
    buy_price = models.DecimalField(verbose_name='Precio de Compra C$', decimal_places=2, max_digits=8, null=False, blank=False)
    buy_price_unit = models.DecimalField(verbose_name='Precio de Compra x Unidad C$', decimal_places=2, max_digits=8, null=False, blank=False)
    sell_price_unit = models.DecimalField(verbose_name='Precio de Venta x Unidad C$', decimal_places=2, max_digits=8, null=False, blank=False)
    total_quantity = models.DecimalField(verbose_name='Cantidad Total', decimal_places=2, max_digits=8, null=False, blank=False)
    actual_quantity = models.DecimalField(verbose_name='Cantidad Actual', decimal_places=2, max_digits=8, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='inventory_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='inventory_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Unidad Medida')
    def get_unit(self):
        return self.product.unit.name
    
    def product_desc(self):
        return '{} Cantidad:{}'.format(self.product, self.quantity)
    
    @admin.display(description='Ganancia Total C$')
    def total_earns_by_product(self):
        return '{0:.2f}'.format((self.sell_price_unit * (self.quantity * self.product.equivalence)) - (self.buy_price * self.quantity ))

    def __str__(self):
        return '{} Cantidad:{}'.format(self.product, self.quantity)
    
    class Meta:
        ordering = ['product', 'product__brand__name', 'product__color']
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'