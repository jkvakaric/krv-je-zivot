from django.db import models
from django.utils.translation import ugettext_lazy as _
from krvjezivot.users.models import User


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("the user notification is assigned to"))
    text = models.CharField(_("text"), blank=False, max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(_("is seen"), default=False)
    link = models.CharField(
        _("link"), blank=False, max_length=100, default='dashboard')
    faicon = models.CharField(
        _('fa icon'), blank=False, max_length=20, default='warning')
    color = models.CharField(
        _('color'), blank=False, max_length=20, default='yellow')

    class Meta:
        ordering = ['timestamp']
