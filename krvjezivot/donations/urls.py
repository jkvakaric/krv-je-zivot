from django.urls import path

from . import views

app_name = 'donations'

urlpatterns = [
    path(
        'invite/list',
        views.get_donation_invites_list,
        name='donation_invites_list'),
    path(
        'invite/<int:invite_id>/confirm',
        views.donation_invite_confirm,
        name='donation_invite_confirm'),
    path(
        'invite/<int:invite_id>/deny',
        views.donation_invite_delete,
        name='donation_invite_deny'),
    path('qrcode', views.get_qrcode, name='user_qrcode'),
    path('history', views.get_donation_history, name='donation_history'),
]
