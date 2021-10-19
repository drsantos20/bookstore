#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]

