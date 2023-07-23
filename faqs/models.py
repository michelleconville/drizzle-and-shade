from django.db import models


class Faqs(models.Model):
    """"
    Frequently asked questions
    """

    ORDER = 'OR'
    DELIVERY = 'DL'
    ACCOUNT = 'AC'
    PRODUCT = 'PR'
    OTHER = 'OT'

    CATEGORY = [
        ('', 'Select Category ↓'),
        (ORDER, 'Order'),
        (DELIVERY, 'Delivery'),
        (ACCOUNT, 'Account'),
        (PRODUCT, 'Product'),
        (OTHER, 'Other'),
    ]

    class Meta:
        verbose_name_plural = 'Faqs'

    category = models.CharField(max_length=2, choices=CATEGORY)
    questions = models.CharField(max_length=200)
    answers = models.TextField()

    def __str__(self):
        return self.questions
