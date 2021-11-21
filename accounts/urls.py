from django.urls import path
from . import views            #from base import views


urlpatterns = [
    path('', views.home, name="home"),   #dodajemy tutaj takie nazwy jak w pliku views nazywaly sie funkcje. Za pomocą "name możmey uzyc tgo w templatkach bez uzywania zahardkodowanych url patternow"
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>', views.customer, name="customer"), 
    path('create_order/', views.createOrder, name="create_order"),
]