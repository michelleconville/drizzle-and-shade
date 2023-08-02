from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, Review


class ProductViewsTest(TestCase):
    """ Testing Product View """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=19.99,
            quantity=5,
            image_alt='Test Image Alt'
        )

        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            name='Test Review',
            rating=4,
            body='This is a test review.'
        )

    def test_all_products_view(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
