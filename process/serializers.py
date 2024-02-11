from .models import Inventory
from rest_framework import serializers

class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only = True)
    product_color = serializers.CharField(read_only = True)
    product_brand = serializers.CharField(read_only = True)
    product_category = serializers.CharField(read_only = True)
    product_unit = serializers.CharField(read_only = True)
    def create(self, validated_data):
        return Inventory.objects.create(**validated_data)
    
    def update(self, instance, validated_data):        
        instance.save()
        return instance
    
    class Meta:
        model = Inventory
        fields = '__all__'