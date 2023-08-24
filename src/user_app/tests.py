from django.test import TestCase
from django.contrib.auth import get_user_model 


# Create your tests here.
User = get_user_model()

class UserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email="testemail@gmail.com",
            password="password123"
        )
        self.assertEqual(user.email, "testemail@gmail.com")
        self.assertFalse(user.is_verified)
        self.assertTrue(user.check_password("password123"))


    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="adminemail@gmail.com",
            password="adminpassword@gmail.com"
        )

        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_verified)