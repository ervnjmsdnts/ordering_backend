from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.models import Category, Product, Order
from api.serializers import CategorySerializer, ProductSerializer, OrderSerializer
# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order_data = request.data

        new_order = Order.objects.create(
            product=Product.objects.get(name=order_data['product']),
            amount=order_data['amount'],
            back_stock=order_data['back_stock'],
            note=order_data['note']
        )

        new_order.save()
        serializer = OrderSerializer(new_order)

        return Response(serializer.data)
