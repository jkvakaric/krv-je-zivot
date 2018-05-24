from django.shortcuts import render
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

from krvjezivot.administration.forms import DonationEventForm, DonationVenueForm
from krvjezivot.administration.models import DonationEvent, DonationVenue, DonationInvite

# Create your views here.


@require_GET
@login_required
def get_donation_invites_list(request):
    donation_invites_pending = DonationInvite.objects.filter(
        user=request.user, confirmed=False)
    donation_invites_confirmed = DonationInvite.objects.filter(
        user=request.user, confirmed=True)

    return render(
        request, 'donations/invites_list.html', {
            'donation_invites_pending': donation_invites_pending,
            'donation_invites_confirmed': donation_invites_confirmed
        })


@require_POST
@login_required
def donation_invite_confirm(request, invite_id=None, *args, **kwargs):
    pass


@require_POST
@login_required
def donation_invite_delete(request, invite_id=None, *args, **kwargs):
    pass


@require_GET
@login_required
def get_qrcode(request):
    return render(request, 'donations/qrcode.html')
