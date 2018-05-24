from django.contrib import admin

# Register your models here.

from .models import DonationInvite, DonationEvent, DonationVenue

# Register your models here.

admin.site.register(DonationVenue)
admin.site.register(DonationEvent)
admin.site.register(DonationInvite)
