from django.urls import path
from . import views

urlpatterns = [
    path("", views.products_page, name="shop"),
    path("cart/", views.cart_page, name="cart"),
    path("customize/", views.customize_page, name="customize"),

    path("api/products/", views.api_list_products, name="api_products"),
    path("api/cart/", views.api_get_cart, name="api_get_cart"),
    path("api/cart/add/", views.api_add_to_cart, name="api_add_to_cart"),
    path("api/customize/", views.api_save_custom_order, name="api_save_custom_order"),
]
