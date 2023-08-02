from django.test import TestCase
from .models import Faqs


class FaqsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods
        """
        Faqs.objects.create(
            category=Faqs.ORDER,
            questions="How to place an order?",
            answers="To place an order, go to the 'Shop' section and select\
                 the items you want to buy. Then, proceed to the checkout\
                     page and follow the instructions."
        )

    def test_questions_max_length(self):
        """
        Test that the questions field has the correct
        maximum length of 200 characters
        """
        faq = Faqs.objects.get(id=1)
        max_length = faq._meta.get_field('questions').max_length
        self.assertEquals(max_length, 200)

    def test_category_choices(self):
        """
        Test that the available choices for the category field are correct
        and have the expected display values
        """
        choices = dict(Faqs.CATEGORY)
        expected_choices = {
            '': 'Select Category',
            'OR': 'Order',
            'DL': 'Delivery',
            'AC': 'Account',
            'OT': 'Other',
            'PR': 'Product'
        }
        self.assertDictEqual(choices, expected_choices)

    def test_str_representation(self):
        """
        Test that the __str__ method of the model returns
        the correct string representation
        """
        faq = Faqs.objects.get(id=1)
        self.assertEqual(str(faq), "How to place an order?")

    def test_category_default_value(self):
        """
        Test that the category field is correctly set to the default value
        ('') when not explicitly provided during object creation
        """
        faq = Faqs.objects.create(
            questions="Test Question",
            answers="Test Answer"
        )
        self.assertEqual(faq.category, '')

    def test_category_choices_values(self):
        """
        Test that the choices are restricted to the provided category values
        """
        faq = Faqs.objects.create(
            category='INVALID',
            questions="Invalid Category Test Question",
            answers="Test Answer"
        )
        self.assertRaisesMessage(
            ValueError, "'INVALID' is not a valid choice."
        )
