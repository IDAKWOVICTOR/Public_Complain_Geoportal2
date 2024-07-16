# complaints/views.py

from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ComplaintForm
from .models import Complaint
import logging
import json

# Get the logger for this module
logger = logging.getLogger(__name__)

def index(request):
    # Get current month and year
    now = timezone.now()
    current_month = now.month
    current_year = now.year

    # Filter complaints by current month and year
    complaints = Complaint.objects.filter(reported_at__year=current_year, reported_at__month=current_month)

    # Prepare complaints data for JavaScript
    complaints_data = [
        {
            'complaint_type': complaint.complaint_type,
            'description': complaint.description,
            'latitude': complaint.location.y,
            'longitude': complaint.location.x,
            'reported_at': complaint.reported_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for complaint in complaints
    ]

    return render(request, 'complaints/index.html', {
        'complaints': complaints,
        'complaints_json': json.dumps(complaints_data)
    })

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            # Log the form data
            logger.info('Form data: %s', form.cleaned_data)
            
            # Save the form data to the database
            complaint = form.save()
            logger.info('Complaint saved successfully: %s', complaint)

            # Redirect the user to the index page
            return redirect('index')
        else:
            # Log validation errors if the form is not valid
            logger.error('Form errors: %s', form.errors)
    else:
        # If the request method is not POST, create a new instance of the form
        form = ComplaintForm()

    # Render the submit complaint template with the form
    return render(request, 'complaints/submit_complaint.html', {'form': form})


