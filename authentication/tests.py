from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class AuthenticationTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.email = 'test@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

    def test_user_registration(self):
        # Ensure user registration page loads
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        # Simulate user registration with valid data
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Check for successful redirect after registration

        # Verify that the new user has been created
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        # Ensure login page loads
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Simulate user login with valid credentials
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Check for successful redirect after login

        # Verify that the user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_user_login(self):
        # Ensure login page loads
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Simulate user login with valid credentials
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Check for successful redirect after login

        # Verify that the user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)

