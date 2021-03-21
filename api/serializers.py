from rest_framework import serializers
from api.models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all()) 
    class Meta:
        model = Product
        fields = ('id', 'name', 'category')

class OrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Order
        fields = ('id', 'product', 'amount', 'back_stock', 'note','order_date')
        depth = 2