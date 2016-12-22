from django.test import TestCase
from .models import UserProfile, UserProfileManager
from django.contrib.auth import authenticate
from django.test import Client

class TestUserProfile(TestCase):

    def setUp(self):
        UserProfile.objects.all().delete()

    def test_create_user(self):
        u = UserProfile.objects.create_user('user@example.com', 'pass123')
        num = UserProfile.objects.count()

        self.assertEqual(num, 1)
        self.assertTrue(u.is_active)
        self.assertTrue(u.is_authenticated)
        self.assertNotEqual(u.password, 'pass123')


        testlogin = authenticate(email='user@example.com', password='pass456')
        self.assertEqual(testlogin, None)

        successlogin = authenticate(email='user@example.com', password='pass123')
        self.assertNotEqual(successlogin, None)
        self.assertEqual(successlogin.id, 1)


    def test_do_login(self):
        u = UserProfile.objects.create_user('user2@example.com', 'testpass123')

        c = Client()
        response = c.post('/account/login/', {'email': 'user2@example.com', 'password': 'testpass1233'})
        res = str(response.content)
        print(res)

        # self.assertEqual(res, "you are logged in 1")
