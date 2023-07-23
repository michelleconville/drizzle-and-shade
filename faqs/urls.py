from django.urls import path
from . import views

urlpatterns = [
    path('', views.faqs, name='faqs'),
    path('add_faqs/', views.add_faqs, name='add_faqs'),
    path('edit_faqs/<int:item_id>/', views.edit_faqs, name='edit_faqs'),
    path('delete_faqs/<int:item_id>/', views.delete_faqs, name='delete_faqs'),
]
