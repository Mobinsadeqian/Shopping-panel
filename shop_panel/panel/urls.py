from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list,name='product_list'),
    path('login/',auth_views.LoginView.as_view(template_name='panel/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main_page'), name='logout'),
    path('signup/', views.signup, name='signup'),
]