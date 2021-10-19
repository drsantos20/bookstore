#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers


from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True)

