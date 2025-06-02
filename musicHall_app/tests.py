from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class LoginViewTest(TestCase):
    def setUp(self):
        # Cria um usuário para teste
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.login_url = '/login/'

    def test_login_success(self):
        # Testa login com credenciais corretas
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_failure(self):
        # Testa login com credenciais incorretas
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)