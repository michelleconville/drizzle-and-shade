from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration for the Product model
    Staff can see all products and filter them as
    desired
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'image_alt',
        'quantity',
    )

    ordering = ('sku', 'name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the Categories Group model
    """
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the review model
    """
    list_display = (
        'user', 'name',
        'rating', 'created_on',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
