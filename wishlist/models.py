from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    """ Wishlist model to store users favourite books"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name='user_wishlist',
                             null=False, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.product.name


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} in {self.wishlist}"
