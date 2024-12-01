from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.core.paginator import Paginator
from django.contrib import messages

def home(request):
    """Display the home page with navigation options."""
    return render(request, 'home.html')

def service_requests_list(request):
    """View to list all service requests with pagination."""
    requests = ServiceRequest.objects.all()  # Fetch all service requests
    paginator = Paginator(requests, 10)  # Show 10 requests per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the current page of requests
    return render(request, 'service_requests/list.html', {'page_obj': page_obj})

def create_service_request(request):
    """View to create a new service request."""
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service request created successfully!')
            return redirect('service_requests_list')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create.html', {'form': form})

def edit_service_request(request, pk):
    """View to edit an existing service request."""
    service_request = get_object_or_404(ServiceRequest, id=pk)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service request updated successfully!')
            return redirect('service_requests_list')
        else:
            messages.error(request, 'There was an error updating your service request.')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'service_requests/edit.html', {'form': form})

def delete_service_request(request, pk):
    """View to delete a service request."""
    service_request = get_object_or_404(ServiceRequest, id=pk)
    if request.method == 'POST':
        service_request.delete()
        messages.success(request, 'Service request deleted successfully!')
        return redirect('service_requests_list')
    return render(request, 'service_requests/confirm_delete.html', {'request': service_request})
