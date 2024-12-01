from django.db import models

class ServiceRequest(models.Model):
    # Predefined choices for request type
    REQUEST_TYPE_CHOICES = [
        ('Issue', 'Issue'),
        ('Feature', 'Feature Request'),
        ('Query', 'Query'),
        ('Other', 'Other'),
    ]

    # Predefined choices for status
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    # Model fields
    request_type = models.CharField(max_length=100, choices=REQUEST_TYPE_CHOICES)  # Limit to predefined types
    description = models.TextField()  # Detailed description of the request
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Open')  # Current status of the request
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated every time the object is saved

    def __str__(self):
        return f"{self.request_type} - {self.status} (Created: {self.created_at})"
