from django.db import models
from django.utils.translation import ugettext_lazy as _

# from enumfields import EnumField

# Create your models here.


class DonationVenue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("attribute key"), max_length=255)
    address = models.CharField(_("attribute key"), max_length=255)


class DonationEvent(models.Model):
    id = models.AutoField(primary_key=True)
    event_start = models.DatetimeField(_("event start datetime"))
    event_end = models.DatetimeField(_("event end datetime"))
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
