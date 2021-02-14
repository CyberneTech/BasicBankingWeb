from django.urls import path, include
from . import views

urlpatterns = [
    path('transfer/',views.transfer),
    path('view/', views.view),
]