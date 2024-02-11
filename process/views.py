from django.shortcuts import get_object_or_404
from django.db.models import F
from .models import Inventory
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import InventorySerializer
from time import sleep

# Create your views here.

class InventoryViewset(viewsets.ModelViewSet):
    ##HTTP REQUESTS
    ## GET
    def list(self, request):
        try:
            queryset = Inventory.objects.annotate(
                product_name = F("product__name"),
                product_color = F("product__color"),
                product_category = F("product__category__name"),
                product_brand = F("product__brand__name"),
                product_unit = F("product__unit__name"),
            ).filter(is_active = True)
            serializer_class = InventorySerializer(queryset, many=True)
            return Response(serializer_class.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## GET BY ID
    def retrieve(self, request, pk = None):
        try:
            obj = get_object_or_404(Inventory, pk = pk)
            serializer = InventorySerializer(obj)
            return Response(serializer.data)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    
    ## POST
    def create(self, request):
        try:
            request.data['is_active'] = True
            serializer = InventorySerializer(data = request.data)
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
            obj = get_object_or_404(Inventory, pk = pk)
            serializer = InventorySerializer(obj, data = request.data)
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
            obj = get_object_or_404(Inventory, pk = pk)
            obj.is_active = False
            obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            ################## START ERROR #################################
            print(e)
    