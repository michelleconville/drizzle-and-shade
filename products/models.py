from django.db import models
from djrichtextfield.models import RichTextField
from profiles.models import UserProfile
from django.contrib.auth.models import User


class Category(models.Model):
    """ category models """
    class Meta:
        """ add correct plural name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """method to get category friendly name"""
        return str(self.friendly_name)


class Product(models.Model):
    """ Product model """

    STOCK_MESSAGE_POSITION_CHOICES = [
        ('left', 'Top Left'),
        ('right', 'Top Right'),
    ]

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = RichTextField(max_length=10000, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    review_count = models.DecimalField(
        max_digits=6, decimal_places=0, null=True, blank=True, default=0
    )
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(blank=False, null=False, default=0)
    stock_message = models.CharField(max_length=100, blank=True, null=True)
    stock_message_position = models.CharField(
        max_length=5, choices=STOCK_MESSAGE_POSITION_CHOICES,
        default='left'
    )

    # this is for the product page
    def stock_message(self):
        if self.stock <= 3:
            return "Low Stock"
        elif self.stock == 0:
            return "Out of Stock"
        return ""

    def is_low_stock(self):
        low_stock_threshold = 3  # Set your desired threshold value here
        return self.quantity <= low_stock_threshold

    # this message is for the product_detail page
    def low_stock_message(self):
        if self.quantity <= 0:
            return "Out of Stock"
        elif self.is_low_stock():
            return f"Hurry up! Only {self.quantity} left in stock!"
        else:
            return None

    def __str__(self):
        return self.name


class Review(models.Model):
    """ A review model for users to review products """

    RATING = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name='reviews'
        )
    name = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING, default=3)
    body = models.TextField(max_length=1024)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'
