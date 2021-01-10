from django.urls import path
from django.conf.urls import url
from . import views
from .views import remove_item

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('cart/', views.cart, name="cart"),
    path('dashboard/', views.dashboard, name="dashboard"),
    url(r'^remove_item/(?P<pk>\d+)$', remove_item, name='remove_item'),
]
