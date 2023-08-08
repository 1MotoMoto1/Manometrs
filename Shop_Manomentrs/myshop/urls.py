from django.urls import path
from unicodedata import name
from django.urls import path, include
from . import views
app_name = 'myshop'

urlpatterns = [
    path('', views.Shop.as_view()),
    path('category/<slug:slug>/', views.CategoryProducts.as_view(), name='product_list_by_category'),

]