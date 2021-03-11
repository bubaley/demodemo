from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer, OrderListSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_classes = {
        'list': OrderListSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, OrderSerializer)
