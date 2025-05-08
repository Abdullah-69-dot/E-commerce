from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('', views.product_list, name='product_list'),
    path('<slug:cat_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
]