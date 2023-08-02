from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product


class BagViewTests(TestCase):
    def setUp(self):
        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            description='Test description'
        )

    def test_add_to_bag(self):
        # Test adding a product to the bag
        url = reverse('add_to_bag', args=[self.product.pk])
        data = {'quantity': 2, 'redirect_url': reverse('view_bag')}
        response = self.client.post(url, data=data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[-1][0], reverse('view_bag'))

        bag = self.client.session.get('bag', {})
        self.assertIn(str(self.product.pk), bag)
        self.assertEqual(bag[str(self.product.pk)], 2)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), f'Added {self.product.name} to your bag')
