from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('card/', views.card, name='card'),
    path('comnnuity/', views.community, name='community'),    
]
