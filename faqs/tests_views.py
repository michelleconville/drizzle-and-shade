from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Faqs


class FaqsViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            username='testuser', password='testpassword')
        cls.superuser = User.objects.create_superuser(
            username='admin', email='admin@example.com',
            password='adminpassword')
        cls.faq = Faqs.objects.create(
            category=Faqs.ORDER, questions='Test Question',
            answers='Test Answer')

    def setUp(self):
        self.client = Client()

    def test_faqs_view(self):
        url = reverse('faqs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/faqs.html')

    def test_add_faqs_view_authenticated_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        url = reverse('add_faqs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/add_faqs.html')

    def test_add_faqs_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('add_faqs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_edit_faqs_view_authenticated_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        url = reverse('edit_faqs', args=[self.faq.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/edit_faqs.html')

    def test_edit_faqs_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('edit_faqs', args=[self.faq.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_delete_faqs_view_authenticated_superuser(self):
        self.client.login(username='admin', password='adminpassword')
        url = reverse('delete_faqs', args=[self.faq.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Faqs.objects.count(), 0)

    def test_delete_faqs_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete_faqs', args=[self.faq.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Faqs.objects.count(), 1)
