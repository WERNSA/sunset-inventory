from .models import Brand, Category, UnitMeasurement, Product
from rest_framework import serializers

class BrandSerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)
    def create(self, validated_data):
        return Brand.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name =  validated_data.get('name', instance.name)
        instance.is_active =  validated_data.get('is_active', instance.is_active)
        instance.updated_by =  validated_data.get('updated_by', instance.updated_by)
        instance.updated_at =  validated_data.get('updated_at', instance.updated_at)
        
        instance.save()
        return instance
    
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name =  validated_data.get('name', instance.name)
        instance.is_active =  validated_data.get('is_active', instance.is_active)
        instance.updated_by =  validated_data.get('updated_by', instance.updated_by)
        instance.updated_at =  validated_data.get('updated_at', instance.updated_at)
        
        instance.save()
        return instance
    
    class Meta:
        model = Category
        fields = '__all__'


class UnitMeasurementSerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return UnitMeasurement.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name =  validated_data.get('name', instance.name)
        instance.is_active =  validated_data.get('is_active', instance.is_active)
        instance.updated_by =  validated_data.get('updated_by', instance.updated_by)
        instance.updated_at =  validated_data.get('updated_at', instance.updated_at)
        
        instance.save()
        return instance
    
    class Meta:
        model = UnitMeasurement
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)
    unit_measurement_id = serializers.UUIDField(read_only=True)
    category_id = serializers.UUIDField(read_only=True)
    brand_id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.category = validated_data.get('category', instance.category)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.equivalence = validated_data.get('equivalence', instance.equivalence)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.color = validated_data.get('color', instance.color)
        instance.name =  validated_data.get('name', instance.name)


        instance.is_active =  validated_data.get('is_active', instance.is_active)
        instance.updated_by =  validated_data.get('updated_by', instance.updated_by)
        instance.updated_at =  validated_data.get('updated_at', instance.updated_at)
        
        instance.save()
        return instance
    
    class Meta:
        model = Product
        fields = '__all__'