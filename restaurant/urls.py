from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
]
