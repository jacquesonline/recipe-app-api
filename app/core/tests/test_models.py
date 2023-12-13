"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


# class ModelTests(TestCase):
class ModelTests(TestCase):
    """Test models"""


# def test_create_user_with_email_successful(self):
    def test_email(self):
        """Test creating a user with an email is successfull"""
        email = 'test@example.com'
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))
        print('testing user and email')
