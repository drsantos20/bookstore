#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory
from product.models import Product
from order.models import Order


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.category = CategoryFactory(title='technology')
        self.product = ProductFactory(title='mouse', price=100, category=[self.category])

    def test_order(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)[0]

        self.assertEqual(product_data['title'], self.product.title)
        self.assertEqual(product_data['price'], self.product.price)
        self.assertEqual(product_data['active'], self.product.active)

    def test_create_order(self) -> None:
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({
            'user': user.id,
            'product': [{
                'id': product.id
            }],
        })

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        import pdb; pdb.set_trace()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)


