# complaints/forms.py

from django import forms
from .models import Complaint
from django.contrib.gis.geos import Point

class ComplaintForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Complaint
        fields = ['complaint_type', 'description', 'image', 'latitude', 'longitude']

    def save(self, commit=True):
        instance = super(ComplaintForm, self).save(commit=False)
        lat = self.cleaned_data.get('latitude')
        lon = self.cleaned_data.get('longitude')
        if lat and lon:
            instance.location = Point(lon, lat)
        if commit:
            instance.save()
        return instance
