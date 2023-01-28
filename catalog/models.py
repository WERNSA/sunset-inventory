import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)

    name = models.CharField(verbose_name='Nombre', max_length=30, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='brand_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='brand_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)

    name = models.CharField(verbose_name='Nombre', max_length=30, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='category_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='category_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)

    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=False, blank=False)

    name = models.CharField(verbose_name='Nombre', max_length=30, null=False, blank=False)
    description = models.CharField(verbose_name='Descripción', max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='product_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='product_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'