from django.db import models
from djrichtextfield.models import RichTextField


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

    def __str__(self):
        return self.name
