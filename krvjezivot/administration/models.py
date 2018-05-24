from django.db import models
from django.utils.translation import ugettext_lazy as _

from krvjezivot.users.models import User

# Create your models here.


class DonationVenue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("donation venue name"), max_length=255)
    address = models.CharField(_("donation venue address"), max_length=255)
    average_recall = models.FloatField(
        _('average recall percentage'), default=1.0)


class DonationEvent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("event name"), max_length=255)
    event_start = models.CharField(
        _("event start date and time"), max_length=255)
    event_end = models.CharField(_("event end date and time"), max_length=255)
    venue = models.ForeignKey(
        DonationVenue,
        on_delete=models.CASCADE,
        verbose_name=_("donation venue"),
        related_name='donation_event')


class DonationInvite(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(
        DonationEvent,
        on_delete=models.CASCADE,
        verbose_name=_("donation event"),
        related_name='donation_invite')
    confirmed = models.BooleanField(
        _('invitation is confirmed'), default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name=_("user"),
        related_name='user_invites',
        null=True)
