from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST, require_GET

from krvjezivot.users.models import User
from krvjezivot.users.enums import Sex

from .forms import DonationEventForm, DonationVenueForm
from .models import DonationEvent, DonationVenue, DonationInvite

# Create your views here.


@require_GET
@login_required
def get_donation_venues_list(request):
    donation_venues_list = DonationVenue.objects.all()
    return render(request, 'administration/donation-venues-list.html',
                  {'donation_venues_list': donation_venues_list})


class DonationVenueFormView(LoginRequiredMixin, View):
    form_class = DonationVenueForm
    instance = DonationVenue()
    template_name = 'administration/donation_venue_add_update_partial.html'

    def get(self, request, venue_id=None, *args, **kwargs):
        if venue_id is not None:
            dv = get_object_or_404(DonationVenue, pk=venue_id)
            self.instance = dv
        form = self.form_class(instance=self.instance)
        return render(request, self.template_name, {
            'form': form,
            'venue_id': venue_id
        })

    def post(self, request, venue_id=None, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if venue_id is not None:
                self.instance = get_object_or_404(DonationVenue, pk=venue_id)
                form = self.form_class(request.POST, instance=self.instance)
            form.save()
            return HttpResponseRedirect(
                reverse('administration:donation_venues_list'))
        return render(request, self.template_name, {
            'form': form,
            'venue_id': venue_id
        })


@require_POST
@login_required
def donation_venue_delete(request, venue_id=None, *args, **kwargs):
    if venue_id is not None:
        instance = get_object_or_404(DonationVenue, pk=venue_id)
        instance.delete()
    return HttpResponseRedirect(reverse('administration:donation_venues_list'))


@require_GET
@login_required
def get_donation_events_list(request):
    donation_events_list = DonationEvent.objects.all()
    return render(request, 'administration/donation_events_list.html',
                  {'donation_events_list': donation_events_list})


class DonationEventFormView(LoginRequiredMixin, View):
    form_class = DonationEventForm
    instance = DonationEvent()
    template_name = 'administration/donation_event_add_update_partial.html'

    def get(self, request, event_id=None, *args, **kwargs):
        if event_id is not None:
            de = get_object_or_404(DonationEvent, pk=event_id)
            self.instance = de
        form = self.form_class(instance=self.instance)
        return render(request, self.template_name, {
            'form': form,
            'event_id': event_id
        })

    def post(self, request, event_id=None, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if event_id is not None:
                self.instance = get_object_or_404(DonationEvent, pk=event_id)
                form = self.form_class(request.POST, instance=self.instance)
            evnt = form.save()
            self.send_invitations(request, evnt)
            return HttpResponseRedirect(
                reverse('administration:donation_events_list'))
        return render(request, self.template_name, {
            'form': form,
            'event_id': event_id
        })

    def send_invitations(self, request, evnt):
        users = [
            usr for usr in User.objects.all()
            if usr.get_days_since_last_donation > 90 and usr.sex == Sex.MALE
            or usr.get_days_since_last_donation > 90 and usr.sex == Sex.FEMALE
        ]
        for user in users:
            DonationInvite.objects.create(event=evnt, user=request.user)


@require_POST
@login_required
def donation_event_delete(request, event_id=None, *args, **kwargs):
    if event_id is not None:
        instance = get_object_or_404(DonationEvent, pk=event_id)
        instance.delete()
    return HttpResponseRedirect(reverse('administration:donation_events_list'))
