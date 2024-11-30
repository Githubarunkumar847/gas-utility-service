from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.core.paginator import Paginator  # Import Paginator
from django.contrib import messages

def service_requests_list(request):
    """View to list all service requests with pagination."""
    requests = ServiceRequest.objects.all()  # Fetch all service requests
    paginator = Paginator(requests, 10)  # Show 10 requests per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the current page of requests
    return render(request, 'service_requests/list.html', {'page_obj': page_obj})  # Pass page_obj to the template

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
    service_request = ServiceRequest.objects.get(id=pk)
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
    service_request = ServiceRequest.objects.get(id=pk)
    if request.method == 'POST':
        service_request.delete()
        return redirect('service_requests_list')
    return render(request, 'service_requests/confirm_delete.html', {'request': service_request})
