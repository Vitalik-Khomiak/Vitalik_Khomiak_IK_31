from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='my_app'),
    path('health/', views.health, name='health')
]
