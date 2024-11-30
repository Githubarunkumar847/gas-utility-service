from django.urls import path
from . import views

urlpatterns = [
    # List all service requests (with pagination)
    path('', views.service_requests_list, name='service_requests_list'),  

    # Create a new service request
    path('create/', views.create_service_request, name='create_service_request'),  

    # Edit an existing service request using primary key (pk)
    path('edit/<int:pk>/', views.edit_service_request, name='edit_service_request'),  

    # Delete a service request using primary key (pk)
    path('delete/<int:pk>/', views.delete_service_request, name='delete_service_request'),  
]
