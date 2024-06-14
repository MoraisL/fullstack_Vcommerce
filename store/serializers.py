from rest_framework import serializers
from .models import Profile, Category, Customer, Product, Order

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'date_modified', 'phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'old_cart']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity', 'address', 'phone', 'date', 'status']
