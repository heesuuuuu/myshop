from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),  # ← 이 줄 추가!
    path('add/', views.product_create, name='product_create'),  # ← 이 줄 추가!
]


