from django.urls import path

from . import views

app_name = "smilez"

urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    path('shop/', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop_detail/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact')
]
