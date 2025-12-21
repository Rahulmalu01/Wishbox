from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path("", views.home, name="home"),

    path("products/add/", views.addproduct, name="addproduct"),
    path("products/edit/", views.alterproduct, name="alterproduct"),
    path("products/update/", views.updateproduct, name="updateproduct"),
    path("products/delete/<int:product_id>/", views.deleteproduct, name="deleteproduct"),

    path("orders/", views.vieworder, name="vieworder"),
    path("orders/complete/<str:order_id>/", views.markcompleted, name="markcompleted"),
    path("orders/completed/", views.completedorder, name="completedorder"),
]
