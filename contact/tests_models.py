from django.test import TestCase
from .models import Contact


class ContactModelTest(TestCase):
    """
    Testing Contact Model
    """

    def test_str_representation(self):
        """
        Test that the __str__ method of the
        model returns the expected string
        representation
        """
        contact = Contact.objects.create(
            contact_reason='product_query',
            name='John Doe',
            email='john@example.com',
            subject='Regarding a product',
            message='This is a sample message for testing.',
        )
        self.assertEqual(str(contact), "Contact Message from John Doe")

    def test_default_values(self):
        contact = Contact.objects.create(
            name='Michelle',
            email='michelle@test.com',
            subject='General Inquiry',
            message='Another test message for default values.',
        )
        self.assertEqual(contact.contact_reason, 'general_query')
        self.assertTrue(contact.pending_reply)
        self.assertFalse(contact.marked_as_done)

    def test_choices_for_contact_reason(self):
        """
        Test that the value for the contact_reason field
        is one of the choices defined in CONTACT_REASONS
        """
        contact = Contact.objects.create(
            contact_reason='other',
            name='Michelle',
            email='michelle@test.com',
            subject='Test Subject',
            message='This is a test message',
        )
        choices = [choice[0] for choice in Contact._meta.get_field(
            'contact_reason').choices]
        self.assertIn(contact.contact_reason, choices)

    def test_blank_fields(self):
        """
        Tests that the blank fields are saved as empty
        strings in the database
        """
        contact = Contact.objects.create(
            name='Empty Fields',
            email='empty@example.com',
            subject='',
            message='',
        )
        self.assertEqual(contact.subject, '')
        self.assertEqual(contact.message, '')
