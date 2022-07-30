from rest_framework import status
from rest_framework.test import APITestCase


# Test Restaurant View
class RestaurantTestCase(APITestCase):

    def test_registration(self):
        data = {"name": "testres", "street": "teststrett"}
        response = self.client.post("/api-restaurant/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
