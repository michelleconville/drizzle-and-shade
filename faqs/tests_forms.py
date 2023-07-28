from django.test import TestCase
from .forms import FaqsForm


class FaqsFormTest(TestCase):

    def test_form_fields(self):
        form = FaqsForm()
        self.assertTrue('category' in form.fields)
        self.assertTrue('questions' in form.fields)
        self.assertTrue('answers' in form.fields)

    def test_form_widget_classes(self):
        form = FaqsForm()
        self.assertEqual(
            form.fields['category'].widget.attrs['class'],
            "border-blue rounded-0")
        self.assertEqual(
            form.fields['questions'].widget.attrs['class'],
            "border-blue rounded-0")
        self.assertEqual(
            form.fields['answers'].widget.attrs['class'],
            "border-blue rounded-0")

    def test_form_widget_ids(self):
        form = FaqsForm()
        self.assertEqual(
            form.fields['category'].widget.attrs['id'], "category-field")
        self.assertEqual(
            form.fields['questions'].widget.attrs['id'], "questions-field")
        self.assertEqual(
            form.fields['answers'].widget.attrs['id'], "answers-field")

    def test_form_widget_aria_labelledby(self):
        form = FaqsForm()
        self.assertEqual(
            form.fields['category'].widget.attrs['aria-labelledby'],
            "category-field-label")
        self.assertEqual(
            form.fields['questions'].widget.attrs['aria-labelledby'],
            "questions-field-label")
        self.assertEqual(
            form.fields['answers'].widget.attrs['aria-labelledby'],
            "answers-field-label")
