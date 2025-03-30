from rest_framework import serializers
from .models import Product, Category
class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        field = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        field = '__all__'