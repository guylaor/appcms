from django.test import TestCase
from .models import UserProfile, UserProfileManager

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


        print(dir(u))
