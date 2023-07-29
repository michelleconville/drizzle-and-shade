from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('order_list/', views.order_list, name='order_list'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),

]
