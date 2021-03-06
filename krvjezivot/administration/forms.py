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
        self.fields['venue'].choices = [
            (v.pk, v.name) for v in DonationVenue.objects.all()
        ]

        self.fields['event_start'].widget.attrs['class'] = 'im-datetime'
        self.fields['event_end'].widget.attrs['class'] = 'im-datetime'
        self.fields['venue'].widget.attrs['class'] = 'select2'
