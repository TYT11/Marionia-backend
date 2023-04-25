from rest_framework import serializers
from .models import Product, Order, OrderDetail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'img', 'stock', 'price', 'category']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['created', 'status', 'total', 'id', 'name']
    # def create(self, validated_data):


class OrderDetailSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source="item.title")

    class Meta:
        model = OrderDetail
        fields = ['item', 'price', 'qty', 'title']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], password=validated_data['password'])
        return user
