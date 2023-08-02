from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm


class TestContactViews(TestCase):
    """
    Testing Contact View
    """

    def test_contact_page_renders(self):
        """
        Test that contact view renders correct page
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")

    def test_contact_message(self):
        """
        Test that contact message works
        """
        contact_data = {
            "contact_reason": "other",
            "name": "Michelle",
            "email": "michelle@test.com",
            "subject": "Test Subject",
            "message": "This is a test message.",
        }
        response = self.client.post(reverse("contact"), data=contact_data)

        form = ContactForm(contact_data)
        self.assertTrue(form.is_valid(), form.errors)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_contact_message_invalid_data(self):
        """
        Test that contact message wont work with invalid data
        """
        contact_data = {
            "contact_reason": "test",
            "name": "Michelle",
            "email": "michelle@test.com",
            "subject": "Test Subject",
            "message": "This is a test message.",
        }
        response = self.client.post(reverse("contact"), data=contact_data)

        form = ContactForm(contact_data)
        self.assertFalse(form.is_valid())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
