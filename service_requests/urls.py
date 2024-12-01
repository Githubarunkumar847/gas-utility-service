# service_requests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.service_requests_list, name='service_requests_list'),
    path('create/', views.create_service_request, name='create_service_request'),
    path('edit/<int:pk>/', views.edit_service_request, name='edit_service_request'),
    path('delete/<int:pk>/', views.delete_service_request, name='delete_service_request'),
]
