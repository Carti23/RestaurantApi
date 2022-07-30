from django.test import TestCase
from .models import Restaurant, Menu


# Test model
class TestRestaurantModel(TestCase):

    def test_should_create_restaurant(self):
        restaurant = Restaurant.objects.create(
            name="Test", street="teststreet")
        restaurant.save()
        self.assertEqual(str(restaurant), 'Test')
