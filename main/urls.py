from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('home', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('individual_product', views.individual_product, name='individual_product'),
    path('cart', views.cart, name='cart'),   
]