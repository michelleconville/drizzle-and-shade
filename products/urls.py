from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit_category/<int:category_id>/',
         views.edit_category, name='edit_category'),
    path(
        'delete/<int:product_id>/', views.delete_product, name='delete_product'
        ),
    path('delete_category/<int:category_id>/',
         views.delete_category, name='delete_category'),
    path(
        'edit_review/<int:review_id>/',
        views.edit_review, name='edit_review'),
    path(
        'delete_review/<int:review_id>/',
        views.delete_review, name='delete_review'),
]
