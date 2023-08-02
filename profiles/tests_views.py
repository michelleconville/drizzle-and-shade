from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order


class ProfileViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="michelle", password="password"
        )
        self.user2 = User.objects.create_user(
            username="emma", password="password_non_superuser"
        )
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.order = Order.objects.create(
            order_number="12345678",
            user_profile=self.profile,
        )

    def test_profile_view_get(self):
        """
        Unit tests for profile view
        """
        self.client.login(username='michelle', password='password')

        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_order_history_view(self):
        """
        Unit tests for order history view
        """
        self.client.login(username="sean", password="password")
        response = self.client.get(
            reverse("order_history", args=[self.order.order_number])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
        self.assertEqual(response.context["order"], self.order)
        self.assertTrue(response.context["from_profile"])

    def test_product_management_view_superuser(self):
        """
        Unit tests for product management page view
        if staff user
        """
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username='michelle', password='password')
        response = self.client.get(reverse('product_management'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/product_management.html')

    def test_product_management_view_non_superuser(self):
        """
        Unit tests for product management page view
        if regular user
        """

        self.client.login(username='emma', password='password_non_superuser')
        response = self.client.get(reverse('product_management'))
        self.assertEqual(response.status_code, 302)
        expected_url = reverse('home')
        self.assertRedirects(response, expected_url)

    def test_account_overview_view(self):
        """
        Unit tests for account overview page view
        """
        self.client.login(username='michelle', password='password')
        response = self.client.get(reverse('account_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/account_overview.html')
