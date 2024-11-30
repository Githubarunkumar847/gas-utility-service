from django.db import models

class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('Issue', 'Issue'),
        ('Feature', 'Feature Request'),
        ('Query', 'Query'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    request_type = models.CharField(max_length=100, choices=REQUEST_TYPE_CHOICES)
    description = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return f"{self.request_type} - {self.status}"
