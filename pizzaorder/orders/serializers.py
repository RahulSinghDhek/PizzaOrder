from rest_framework import serializers

from orders.models import PizzaOrders,Customer,Pizza



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'customer_id', 'name', 'address',
        )

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            'id', 'type', 'size',
        )


class OrdersSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(many=True)

    class Meta:
        model = PizzaOrders
        fields = (
            'id','created_time', 'customer','status',
        )

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        pizza_data = validated_data.pop('pizza')
        orders = PizzaOrders.objects.create(**validated_data)
        orders.create(*customer_data)
        orders.set_pizza(*pizza_data)

        return orders
#
# class PizzaOrdersSerializers(serializers.ModelSerializer):
#     orderdata = OrdersSerializer(many=True)
#     pizza =
#
#     class Meta:
#         model = OrderData
#         fields = (
#             'id','pizza', 'orderdata','quantity',
#         )



