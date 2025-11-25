from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list,name='product_list')
]