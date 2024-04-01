from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterViewTests(TestCase):
    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_register_view_post_valid_form(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_view_post_invalid_form(self):
        data = {}  # Empty data, should fail validation
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # Should remain on the registration page
        self.assertFormError(response, 'form', 'username', 'This field is required')

class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_view_post_valid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_view_post_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)  # Should remain on the login page
        self.assertFalse('_auth_user_id' in self.client.session)