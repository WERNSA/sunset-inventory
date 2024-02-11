from django.contrib import admin
from process.models import Inventory
from django.db.models import Sum

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):        
        obj.created_by = request.user

        obj.buy_price_unit = obj.buy_price / obj.product.equivalence
        obj.sell_price_unit = obj.buy_price_unit + obj.profit_unit
        obj.total_quantity = obj.quantity * obj.product.equivalence        
        if not obj.updated_by:
            obj.updated_by = request.user
            obj.actual_quantity = obj.total_quantity
        super().save_model(request, obj, form, change)
    

    exclude = ('id','is_active','created_by', 'updated_by', 'buy_price_unit', 'sell_price_unit', 'total_quantity')

    list_display = ('product', 'sell_price_unit', 'get_unit', 'total_quantity', 'actual_quantity', 'buy_price', 'total_earns_by_product')

    search_fields = ('product__name', 'product__category__name', 'product__color', 'product__brand__name')

    # list_filter = ('product__category__name',)