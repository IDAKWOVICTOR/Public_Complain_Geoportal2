# complaints/models.py

from django.contrib.gis.db import models

class Complaint(models.Model):
    COMPLAINT_TYPES = [
        ('Accident', 'Accident'),
        ('Water Leakage', 'Water Leakage'),
        ('Pothole', 'Pothole'),
        ('Borehole', 'Borehole'),
        ('Broken Facility', 'Broken Facility'),
        ('Power Outages', 'Power Outages'),
        ('Poor Road Conditions', 'Poor Road Conditions'),
        ('Traffic Congestion', 'Traffic Congestion'),
        ('Inadequate Public Transportation', 'Inadequate Public Transportation'),
        ('Water Supply Issues', 'Water Supply Issues'),
        ('Inconsistent Waste Collection', 'Inconsistent Waste Collection'),
        ('Poor Healthcare Services', 'Poor Healthcare Services'),
        ('Lack of Security', 'Lack of Security'),
        ('Corruption in Public Offices', 'Corruption in Public Offices'),
        ('Unemployment', 'Unemployment'),
        ('Poor Educational Facilities', 'Poor Educational Facilities'),
        ('Noise Pollution', 'Noise Pollution'),
        ('Air Pollution', 'Air Pollution'),
        ('Poor Drainage Systems', 'Poor Drainage Systems'),
        ('Inadequate Housing', 'Inadequate Housing'),
        ('Illegal Land Grabbing', 'Illegal Land Grabbing'),
        ('Bureaucratic Delays', 'Bureaucratic Delays'),
        ('Harassment by Law Enforcement', 'Harassment by Law Enforcement'),
        ('Poor Internet Connectivity', 'Poor Internet Connectivity'),
        ('Inconsistent Postal Services', 'Inconsistent Postal Services'),
        ('High Cost of Living', 'High Cost of Living'),
        ('Environmental Degradation', 'Environmental Degradation'),
        ('Lack of Public Toilets', 'Lack of Public Toilets'),
        ('Poor Street Lighting', 'Poor Street Lighting'),
        ('Overcrowded Public Spaces', 'Overcrowded Public Spaces'),
        ('Inadequate Social Services', 'Inadequate Social Services'),
        ('Poor Sanitation in Markets', 'Poor Sanitation in Markets'),
        ('High Crime Rates', 'High Crime Rates'),
        ('Flooding', 'Flooding'),
        ('Poor Customer Service in Public Offices', 'Poor Customer Service in Public Offices'),
        ('Bribery Demands', 'Bribery Demands'),
        ('Unregulated Street Trading', 'Unregulated Street Trading'),
        ('Poor Maintenance of Public Facilities', 'Poor Maintenance of Public Facilities'),
        ('Lack of Recreational Spaces', 'Lack of Recreational Spaces'),
        ('Stray Animals', 'Stray Animals'),
        ('Poor Urban Planning', 'Poor Urban Planning'),
        ('Noise from Generators', 'Noise from Generators'),
        ('Delayed Justice System', 'Delayed Justice System'),
        ('High Fuel Prices', 'High Fuel Prices'),
        ('Poor Telecom Services', 'Poor Telecom Services'),
        ('Inconsistent Public Transport Schedules', 'Inconsistent Public Transport Schedules'),
        ('Unsafe Building Structures', 'Unsafe Building Structures'),
        ('Poorly Maintained Parks', 'Poorly Maintained Parks'),
        ('Inadequate Fire Service Response', 'Inadequate Fire Service Response'),
    ]

    complaint_type = models.CharField(max_length=50, choices=COMPLAINT_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', null=True, blank=True)
    location = models.PointField(srid=4326)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.complaint_type} at {self.location}"
