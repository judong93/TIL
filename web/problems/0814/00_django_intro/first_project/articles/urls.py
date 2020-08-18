from django.urls import path
from . import views

urlpatters = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('dtl-practice/', views.dtl_practice),
    path('throw/', views.throw),
    path('catch/', views.catch),
]