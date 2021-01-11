from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('reg/', views.reg, name='reg'),
    path('cart/', views.cart, name="cart"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
