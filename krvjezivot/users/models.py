from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from enumfields import EnumField
from datetime import date

from .enums import Sex
from krvjezivot.dontations.enums import BloodGroup, RhesusFactor


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns around the globe.
    full_name = models.CharField(_("Full Name"), blank=True, max_length=255)
    address = models.CharField(_('address'), blank=True, max_length=1024)

    frequency = models.FloatField(_("average number of donations last year"))
    last_donation_date = models.DateField(_("date of last donation"))
    sex = EnumField(Sex, verbose_name=_('sex'), max_length=32)
    blood_group = EnumField(
        BloodGroup, verbose_name=_('blood group'), max_length=32)
    rhesus_factor = EnumField(
        RhesusFactor, verbose_name=_('rhesus factor'), max_length=32)
    distance = models.IntegerField(_('distance to nearest donation venue'))

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_days_since_last_donation(self):
        time_span = self.last_donation_date - date.today()
        return time_span.days

    def get_blood_type(self):
        return self.blood_group + self.rhesus_factor
