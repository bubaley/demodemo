from rest_framework import serializers

from order.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'number')
