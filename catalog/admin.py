from django.contrib import admin

from catalog.models import Brand, Category, Product, UnitMeasurement

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.updated_by:
            obj.updated_by = request.user
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    exclude = ('id','is_active','created_by', 'updated_by')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.updated_by:
            obj.updated_by = request.user
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    exclude = ('id','is_active','created_by', 'updated_by')

@admin.register(UnitMeasurement)
class UnitMeasurementAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.updated_by:
            obj.updated_by = request.user
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    exclude = ('id','is_active','created_by', 'updated_by')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.updated_by:
            obj.updated_by = request.user
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    exclude = ('id','is_active','created_by', 'updated_by')