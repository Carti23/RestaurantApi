from rest_framework import status
from rest_framework.test import APITestCase


# Test Registration
class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testcase", "email": "testcase@gmail.com", "password1": "some_password",
                "password2": "some_password", "first_name": "Test", "last_name": "Case"}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
