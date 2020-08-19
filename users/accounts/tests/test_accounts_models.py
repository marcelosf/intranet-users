from django.test import TestCase
from django.contrib.auth.models import AbstractBaseUser

from users.accounts.models import UserModel


class UserModelTest(TestCase):
    def setUp(self):
        self.obj = UserModel()

    def test_is_instance_of_model(self):
        self.assertIsInstance(self.obj, AbstractBaseUser)

    def test_has_parametters(self):
        parametters = ('login', 'name', 'user_type', 'main_email',
                       'alternative_email', 'usp_email',
                       'formatted_phone', 'wsuserid', 'bind', 'is_staff',
                       'is_active', 'date_joined', 'last_login')
        for expected in parametters:
            with self.subTest():
                message = '{} not found.'.format(expected)
                self.assertTrue(hasattr(self.obj, expected), msg=message)

    def test_has_get_full_name_attribute(self):
        self.assertTrue(hasattr(self.obj, 'get_full_name'))

    def test_has_attribute_get_short_name(self):
        self.assertTrue(hasattr(self.obj, 'get_short_name'))