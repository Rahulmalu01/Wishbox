from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='manager'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('alterproduct/', views.alterproduct, name='alterproduct'),
    path('vieworder/', views.vieworder, name='vieworder'),
    path('completedorder/', views.completedorder, name='completedorder'),
]
