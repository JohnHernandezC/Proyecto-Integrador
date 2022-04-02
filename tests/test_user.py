import pytest
from django.test import TestCase, Client
from UsuariosApp.models import Usuario
from tests.factories import UsuarioAdminFactory, UsuarioComunFactory

class UsuarioTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.common_user = UsuarioComunFactory.create()
        self.superuser = UsuarioAdminFactory.create()
    
    def test_common_user_creation(self):
        self.assertEqual(self.common_user.is_active, True)
        self.assertEqual(self.common_user.is_staff, False)
        self.assertEqual(self.common_user.is_superuser, False)
    
    def test_suerpuser_creation(self):
        self.assertEqual(self.superuser.is_staff, True)
        self.assertEqual(self.superuser.is_superuser, True)

    

    

    

    
    
