from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    def test_valid_form(self):
        """
        Test that the form is valid with valid data
        """
        form_data = {
            "contact_reason": "other",
            "name": "Michelle",
            "email": "michelle@test.com",
            "subject": "Test Subject",
            "message": "This is a test message.",
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_required_fields(self):
        """
        Test that the form is invalid when required fields are missing
        """
        form_data = {
            "contact_reason": "",
            "name": "Michelle",
            "email": "",
            "subject": "Test Subject",
            "message": "",
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_invalid_form_invalid_email(self):
        """
        Test that the form is invalid when an invalid email address is provided
        """
        form_data = {
            "contact_reason": "other",
            "name": "Michelle",
            "email": "invalid_email",
            "subject": "Test Subject",
            "message": "This is a test message.",
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
