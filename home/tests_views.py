# app_name/tests.py
from django.test import TestCase, Client
from django.urls import reverse


class HomepageViewsTest(TestCase):
    """
    Testing Home View
    """

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_privacy_page(self):
        url = reverse('privacy')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/privacy_policy.html')

    def test_terms_page(self):
        url = reverse('terms')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/terms.html')
