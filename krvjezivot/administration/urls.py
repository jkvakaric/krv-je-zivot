from django.urls import path

from . import views

app_name = 'administration'

urlpatterns = [
    path('venue/list', views.get_donation_venues_list, name='donation_venues_list'),
    path('venue/add', views.DonationVenueFormView.as_view(), name='donation_venue_add'),
    path('venue/<int:venue_id>', views.DonationVenueFormView.as_view(), name='donation_venue_details'),
    path('venue/<int:venue_id>/update', views.DonationVenueFormView.as_view(), name='donation_venue_update'),
    path('venue/<int:venue_id>/delete', views.donation_venue_delete, name='donation_venue_delete'),

    path('event/list', views.get_donation_events_list, name='donation_events_list'),
    path('event/add', views.DonationEventFormView.as_view(), name='donation_event_add'),
    path('event/<int:event_id>', views.DonationEventFormView.as_view(), name='donation_event_details'),
    path('event/<int:event_id>/update', views.DonationEventFormView.as_view(), name='donation_event_update'),
    path('event/<int:event_id>/delete', views.donation_event_delete, name='donation_event_delete'),
]
