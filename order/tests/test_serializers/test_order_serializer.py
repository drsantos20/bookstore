#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.product_1 = ProductFactory(title='mouse', price=100)
        self.product_2 = ProductFactory(title='keyboard', price=100)

        self.order = OrderFactory(product=(self.product_1, self.product_2))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data

        self.assertEquals(serializer_data['total'], 200)
        self.assertEquals(serializer_data['product'][0]['title'], 'mouse')
        self.assertEquals(serializer_data['product'][1]['title'], 'keyboard')

