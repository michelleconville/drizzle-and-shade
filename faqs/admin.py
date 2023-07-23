from django.contrib import admin
from .models import Faqs


@admin.register(Faqs)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'questions', 'answers']
