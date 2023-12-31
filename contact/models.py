from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.

CONTACT_REASONS = (
    ("product_query", "Product Query"),
    ("order_query", "Order Query"),
    ("other", "Other"),
)


class Contact(models.Model):
    """A model for Contact Messages"""

    date_received = models.DateTimeField(auto_now_add=True)
    contact_reason = models.CharField(
        max_length=100,
        choices=CONTACT_REASONS,
        default="general_query",
        null=False,
        blank=False,
    )
    name = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=254)
    subject = models.CharField(null=False, blank=False, max_length=50)
    message = RichTextField(max_length=10000, null=False, blank=False)
    pending_reply = models.BooleanField(default=True)
    marked_as_done = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns 'Contact Message from and customer name'
        as a string representation of the object.
        """
        return f"Contact Message from {self.name}"
