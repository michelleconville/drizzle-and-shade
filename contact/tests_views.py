from django.test import TestCase, Client
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
            "contact_reason": "other",  # Use a valid choice here
            "name": "Michelle",
            "email": "michelle@test.com",
            "subject": "Test Subject",
            "message": "This is a test message.",
        }
        response = self.client.post(reverse("contact"), data=contact_data)

        # Check if the form is valid
        form = ContactForm(contact_data)
        self.assertTrue(form.is_valid(), form.errors)

        # Check the response status code and redirect URL
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_contact_message_invalid_data(self):
        """
        Test that contact message wont work with invalid data
        """
        contact_data = {
            "contact_reason": "test",  # Make sure this field is invalid
            "name": "Michelle",
            "email": "michelle@test.com",
            "subject": "Test Subject",
            "message": "This is a test message.",
        }
        response = self.client.post(reverse("contact"), data=contact_data)

        # Check if the form is invalid
        form = ContactForm(contact_data)
        self.assertFalse(form.is_valid())

        # Check the response status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
