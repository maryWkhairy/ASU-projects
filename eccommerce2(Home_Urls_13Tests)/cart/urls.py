from django.urls import path
from . import views
from django.conf.urls import url

from .views import add_to_cart, add_quantity

urlpatterns = [
    path('cart_items/', views.show_items, name='show_items'),
    url(r'^add_to_cart/(?P<pk>\d+)$', add_to_cart, name='add_to_cart'),
    url(r'^add_quantity/(?P<pk>\d+)$', add_quantity, name='add_quantity'),
]