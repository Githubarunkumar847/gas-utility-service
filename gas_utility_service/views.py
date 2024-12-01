from django.shortcuts import render

def home(request):
    """Display the home page with navigation options."""
    return render(request, 'home.html')
