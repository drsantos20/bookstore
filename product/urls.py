#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from product import viewsets

router = routers.SimpleRouter()
router.register(r'product', viewsets.ProductViewSet, basename='product')
router.register(r'category', viewsets.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
