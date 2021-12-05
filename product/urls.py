#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers

from product import viewsets

router = routers.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet, basename="product")
router.register(r"category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
