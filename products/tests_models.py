from django.test import TestCase
from .models import Category, Product, Review
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):
    def test_category_str_method(self):
        category = Category(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_category_get_friendly_name_method(self):
        category = Category(
            name='Test Category', friendly_name='Friendly Category')
        self.assertEqual(category.get_friendly_name(), 'Friendly Category')


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=19.99,
            quantity=5,
            image_alt='Test Image Alt'
        )

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_low_stock_message_method(self):
        self.product.quantity = 0
        self.assertEqual(self.product.low_stock_message(), 'Out of Stock')

        self.product.quantity = 3
        self.assertEqual(
            self.product.low_stock_message(), 'Hurry up! Only 3 left in stock!'
            )

        self.product.quantity = 5
        self.assertIsNone(self.product.low_stock_message())

    def test_product_is_out_of_stock_property(self):
        self.product.quantity = 0
        self.assertTrue(self.product.is_out_of_stock)

        self.product.quantity = 1
        self.assertFalse(self.product.is_out_of_stock)


class ReviewModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=19.99,
            quantity=5,
            image_alt='Test Image Alt'
        )
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            name='Test Review',
            rating=4,
            body='This is a test review.'
        )

    def test_review_str_method(self):
        expected_str = (
            f'Review for {self.product.name} by {self.user.username}')
        self.assertEqual(str(self.review), expected_str)
