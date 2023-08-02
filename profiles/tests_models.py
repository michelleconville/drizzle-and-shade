from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class UserProfileModelTestCase(TestCase):
    def setUp(self):
        """
        Create a test user
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.expected_str = str(self.user.username)

    def test_user_profile_creation(self):
        """
        Test that a UserProfile instance is created when a User is created
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(str(self.profile), self.expected_str)

    def test_user_profile_signal(self):
        """
        Test that a UserProfile instance is created for a new User via signal
        """
        new_user = User.objects.create_user(
            username='newuser', password='newpassword')
        self.assertTrue(hasattr(new_user, 'userprofile'))
        self.assertIsInstance(new_user.userprofile, UserProfile)

    def test_user_profile_signal_existing_user(self):
        """"
        Test that a UserProfile instance is updated for an
        existing User via signal
        """
        existing_user = User.objects.create_user(
            username='existinguser', password='existingpassword')
        existing_user.userprofile.default_phone_number = '1234567890'
        existing_user.save()

        updated_user_profile = UserProfile.objects.get(user=existing_user)

        self.assertEqual(
            updated_user_profile.default_phone_number, '1234567890')
