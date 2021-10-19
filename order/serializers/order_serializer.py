#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = ['product']


