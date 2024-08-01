"""test for models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):
    """test for models"""

    def test_create_user_with_email(self):
        """Test creating a new user with email is successful"""

        email = 's@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
           email=email,
           password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))