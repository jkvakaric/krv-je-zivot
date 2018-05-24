from django import forms

from .models import DonationEvent, DonationVenue


class DonationVenueForm(forms.ModelForm):
    class Meta:
        model = DonationVenue
        fields = ['name', 'address']


class DonationEventForm(forms.ModelForm):
    class Meta:
        model = DonationEvent
        fields = ['name', 'event_start', 'event_end', 'venue']

    def __init__(self, *args, **kwargs):
        super(DonationEventForm, self).__init__(*args, **kwargs)
        self.fields['event_start'].widget.attrs['class'] = 'datepicker'
        self.fields['event_end'].widget.attrs['class'] = 'datepicker'
        self.fields['venue'].widget.attrs['class'] = 'select2'
