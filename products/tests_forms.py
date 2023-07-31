from django.test import TestCase
from django import forms
from .forms import ProductForm, CategoryForm, ReviewForm, UpdateStockForm
from .models import Category, Product, Review


class CategoryFormTest(TestCase):
    def test_category_form_valid_data(self):
        form_data = {
            'name': 'Test Category',
            'friendly_name': 'Friendly Test Category',
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_empty_data(self):
        form = CategoryForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class ReviewFormTest(TestCase):
    def test_review_form_valid_data(self):
        product = Product.objects.create(
            name='Test Product',
            price=19.99,
            quantity=5,
        )
        form_data = {
            'rating': 4,
            'body': 'This is a test review.',
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_empty_data(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


class UpdateStockFormTest(TestCase):
    def test_update_stock_form_valid_data(self):
        product = Product.objects.create(
            name='Test Product',
            price=19.99,
            quantity=5,
        )
        form_data = {
            'quantity': 10,
        }
        form = UpdateStockForm(data=form_data, instance=product)
        self.assertTrue(form.is_valid())
