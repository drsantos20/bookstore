#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import include, path
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]
