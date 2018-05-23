from django.db import models
from django.utils.translation import ugettext_lazy as _
# from enumfields import EnumField

# Create your models here.


class DonationVenue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("attribute key"), max_length=255)
    address = models.CharField(_("attribute key"), max_length=255)
