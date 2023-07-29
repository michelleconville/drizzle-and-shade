from django.test import TestCase
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User


class TestUserProfileForm(TestCase):
    """Testing UserProfile Form"""

    def setUp(self):
        """
        Setup Method
        """
        self.user = User.objects.create_user(
            username="michelle", email="michelle@test.com", password="password"
        )

    def test_userprofileform_valid(self):
        """
        Test UserProfile form is valid
        """
        form = UserProfileForm(
            {
                "user": self.user,
                "default_phone_number": "123456789",
                "default_street_address1": "1 test house",
                "default_street_address2": "1 test street",
                "default_town_or_city": "test city",
                "default_county": "test county",
                "default_postcode": "a12 p567",
                "default_country": "IE",
            }
        )
        self.assertTrue(form.is_valid())

    def test_userprofileform_not_valid(self):
        """
        Test UserProfile form is not valid
        """
        form = UserProfileForm(
            {
                "user": self.user,
                "default_phone_number": "123456789",
                "default_street_address1": str("a" * 81),
                "default_street_address2": "1 test street",
                "default_town_or_city": "test city",
                "default_county": "test county",
                "default_postcode": "v12 y934",
                "default_country": "IE",
            }
        )
        self.assertIn("default_street_address1", form.errors.keys())
        self.assertEqual(
            form.errors["default_street_address1"][0],
            "Ensure this value has at most 80 characters (it has 81).",
        )
        self.assertFalse(form.is_valid())
