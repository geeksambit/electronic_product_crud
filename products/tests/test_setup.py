from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.products_url = reverse('products')

        self.product_data = {
            "name" : "test mobile",
            "description" : "test mobile desc",
            "type":"Mob"
        }

        return super().setUp()


    def tearDown(self):

        return super().setUp()