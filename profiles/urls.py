from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path(
        'product_management/', views.product_management,
        name='product_management'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('account_overview/', views.account_overview, name='account_overview'),
    path("delete/<username>/", views.delete_profile, name="delete_profile"),
]
