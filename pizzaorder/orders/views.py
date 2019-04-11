from orders.models import PizzaOrders,Pizza,Customer,Orders
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from orders.serializers import PizzaSerializer,CustomerSerializer, OrdersSerializer


class PizzaViewSet(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class CustomerViewSet(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderDataViewSet(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
