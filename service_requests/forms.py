from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'status']
        widgets = {
            'request_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    # Custom validation for description field
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:  # Minimum description length validation
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description

    # Custom validation for status field (if required)
    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in ['Open', 'In Progress', 'Closed']:  # Assuming these are valid statuses
            raise forms.ValidationError("Invalid status selected.")
        return status
