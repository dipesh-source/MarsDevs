from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import VendorSerializers, ConsumerSerializers
from .models import Vendor, Consumer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import VendorFilterSet, ConsumerFilterSet


class Vendor_data(ModelViewSet):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.all()

    filter_class = VendorFilterSet

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_fields = ['name','email']
    search_fields = ['name','email']
    ordering_fields = ['__all__']

    def get_queryset(self):
        return Vendor.objects.all()


class Consumer_data(ModelViewSet):
    serializer_class = ConsumerSerializers
    queryset = Consumer.objects.all()

    filter_class = ConsumerFilterSet
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name','email','age']
    search_fields = ['name','email']
    ordering_fields = ['__all__']


    @action(detail=True, methods=['DELETE'])
    def remove_data(self, request, pk=None):
        try:
            obj = Consumer.objects.get(pk=pk)
            obj.delete()
            return Response({'data':'Data Deleted'}, status=status.HTTP_200_OK)
        except Consumer.DoesNotExist:
            return False