#!/usr/bin/env python
# -*- coding: utf-8 -*-


from rest_framework.viewsets import ModelViewSet

from order.models import Order 
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


