from django.test import TestCase
from django.contrib.auth.models import User


# Test User models
class TestUserModel(TestCase):

    def test_should_create_user(self):
        user = User.objects.create_user(
            username="test", email="test@gmail.com")
        user.set_password('password12')
        user.save()
        self.assertEqual(str(user), 'test')
