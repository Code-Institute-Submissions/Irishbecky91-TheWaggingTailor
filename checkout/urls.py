"""
Checkout URLs
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_successful/<order_number>', views.checkout_successful,
         name='checkout_successful'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
]
