from django.contrib import admin
from . models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """wishlist admin"""
    model = Wishlist
    fields = ('user', 'product')
    list_display = ('pk', 'user', 'product')


admin.site.register(Wishlist, WishlistAdmin)
