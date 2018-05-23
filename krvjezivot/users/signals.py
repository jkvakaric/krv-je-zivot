# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from django.dispatch import receiver

from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import social_account_added


@receiver(user_signed_up)
def add_full_name_for_new_user(sender, user, **kwargs):
    user.full_name = user.username
    user.save()


@receiver(social_account_added)
def add_setting_for_social_account(sender, sociallogin, **kwargs):
    pass
