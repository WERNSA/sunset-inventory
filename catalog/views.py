from django.shortcuts import get_object_or_404
from .models import Brand, Category, UnitMeasurement, Product
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import BrandSerializer, CategorySerializer, UnitMeasurementSerializer, ProductSerializer
from django.db.models import F

# Create your views here.

class BrandViewset(viewsets.ModelViewSet):
    ##HTTP REQUESTS
    ## GET
    def list(self, request):
        try:
            queryset = Brand.objects.annotate(
                key = F('id')
            )
            serializer_class = BrandSerializer(queryset, many=True)
            return Response(serializer_class.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## GET BY ID
    def retrieve(self, request, pk = None):
        try:
            obj = get_object_or_404(Brand, pk = pk)
            serializer = BrandSerializer(obj)
            return Response(serializer.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## POST
    def create(self, request):
        try:
            request.data['is_active'] = True
            serializer = BrandSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)

    ## PUT
    def update(self, request, pk = None):
        try:
            obj = get_object_or_404(Brand, pk = pk)
            serializer = BrandSerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## DELETE
    def destroy(self, request, pk = None):
        try:
            obj = get_object_or_404(Brand, pk = pk)
            obj.is_active = False
            obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            ################## START ERROR #################################
            print(e)



class CategoryViewset(viewsets.ModelViewSet):
    ##HTTP REQUESTS
    ## GET
    def list(self, request):
        try:
            queryset = Category.objects.annotate(
                key = F('id')
            )
            serializer_class = CategorySerializer(queryset, many=True)
            return Response(serializer_class.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## GET BY ID
    def retrieve(self, request, pk = None):
        try:
            obj = get_object_or_404(Category, pk = pk)
            serializer = CategorySerializer(obj)
            return Response(serializer.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## POST
    def create(self, request):
        try:
            request.data['is_active'] = True
            serializer = CategorySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)

    ## PUT
    def update(self, request, pk = None):
        try:
            obj = get_object_or_404(Category, pk = pk)
            serializer = CategorySerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## DELETE
    def destroy(self, request, pk = None):
        try:
            obj = get_object_or_404(Category, pk = pk)
            obj.is_active = False
            obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    

    
class UnitMeasurementViewset(viewsets.ModelViewSet):
    ##HTTP REQUESTS
    ## GET
    def list(self, request):
        try:
            queryset = UnitMeasurement.objects.annotate(
                key = F('id')
            )
            serializer_class = UnitMeasurementSerializer(queryset, many=True)
            return Response(serializer_class.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## GET BY ID
    def retrieve(self, request, pk = None):
        try:
            obj = get_object_or_404(UnitMeasurement, pk = pk)
            serializer = UnitMeasurementSerializer(obj)
            return Response(serializer.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## POST
    def create(self, request):
        try:
            request.data['is_active'] = True
            serializer = UnitMeasurementSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)

    ## PUT
    def update(self, request, pk = None):
        try:
            obj = get_object_or_404(UnitMeasurement, pk = pk)
            serializer = UnitMeasurementSerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## DELETE
    def destroy(self, request, pk = None):
        try:
            obj = get_object_or_404(UnitMeasurement, pk = pk)
            obj.is_active = False
            obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    

    
class ProductViewset(viewsets.ModelViewSet):
    ##HTTP REQUESTS
    ## GET
    def list(self, request):
        try:
            queryset = Product.objects.values(
                'id',
                'name',
                'description',
                'color',
                'is_active',
                'created_at',
                'brand',
                'category',
                'unit'
            ).annotate(
                key = F('id'),
                brand_name = F('brand__name'),
                category_name = F('category__name'),
                unit_name = F('unit__name'),
            )
            # serializer_class = ProductSerializer(queryset, many=True)
            return Response(queryset)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## GET BY ID
    def retrieve(self, request, pk = None):
        try:
            obj = get_object_or_404(Product, pk = pk)
            serializer = ProductSerializer(obj)
            return Response(serializer.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## POST
    def create(self, request):
        try:
            request.data['is_active'] = True
            serializer = ProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)

    ## PUT
    def update(self, request, pk = None):
        try:
            obj = get_object_or_404(Product, pk = pk)
            serializer = ProductSerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## DELETE
    def destroy(self, request, pk = None):
        try:
            obj = get_object_or_404(Product, pk = pk)
            obj.is_active = False
            obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    