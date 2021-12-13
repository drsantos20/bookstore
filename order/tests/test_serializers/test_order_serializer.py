from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        self.order = OrderFactory(product=(self.product_1, self.product_2))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEquals(
            serializer_data["product"][0]["title"], self.product_1.title)
        self.assertEquals(
            serializer_data["product"][1]["title"], self.product_2.title)
