from django.contrib import admin
from .models import Faqs


@admin.register(Faqs)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the FAQ model
    """
    list_display = ['category', 'questions', 'answers']
