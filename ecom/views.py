from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Product, Order, OrderDetail
from rest_framework import viewsets
from .serializers import ProductSerializers, UserSerializer, OrderSerializers, OrderDetailSerializer
from django.contrib.auth.models import User
import json

# Create your views here.


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers

    def get_queryset(self):
        queryset = Product.objects.all()
        search_word = self.request.query_params.get('q', None)
        if search_word:
            queryset = queryset.filter(title__icontains=search_word)
        return queryset


class UserViewSet(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderViewSet(APIView):
    serializer_class = OrderSerializers
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        orders = Order.objects.filter(user=user).values()
        return Response(orders, status=200)

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        print(request.data[0])
        order = Order.objects.create(
            user=user, phone=request.data[0]["phone"], address=request.data[0]["address"], total=request.data[0]["total"], name=request.data[0]['name'])
        order.save()
        for item in request.data:
            print(item)
            serializer = OrderDetailSerializer(data=item)
            if serializer.is_valid():
                serializer.save(order=order)

            else:
                return Response(serializer.errors, status=400)
        return Response(serializer.data, status=201)


class OrderDeleteViewSet(APIView):
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        order_id = request.data['order']
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response({"status": "200", "data": "Success"})


class OrderDetailViewSet(APIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.user.id
        order_num = request.GET['n']
        order = Order.objects.filter(user=user, id=order_num)
        if order:
            order_detail = OrderDetail.objects.filter(order=order_num)
            serialized = OrderDetailSerializer(order_detail, many=True)
            print(serialized.data)

            return Response(serialized.data, status=200)
        return Response({"status": 'error', "data": "NO"})
