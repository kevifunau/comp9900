from django.conf.urls import url
from . import views

app_name = 'PendingAndBooking'
urlpatterns = [
    url(r'^$', views.booking, name='booking'),
    url(r'^(?P<trip_id>[0-9]+)/paynow/', views.paynow, name='paynow'),
    url(r'^(?P<trip_id>[0-9]+)/payment/', views.payment, name='payment'),
    url(r'^trips/', views.trips, name='trips'),
    url(r'^trans/', views.my_trans, name='my_trans'),
    url(r'^(?P<tran_id>[0-9]+)confirm/', views.confirm, name='confirm'),

    url(r'^pending/', views.pending, name='pending'),
    url(r'^(?P<trip_id>[0-9]+)/pending_request/', views.pending_request, name='pending_request'),
    url(r'^add_pending/', views.add_pending, name='add_pending'),
    url(r'^(?P<tran_id>[0-9]+)/show_pending/', views.show_pending, name='show_pending'),
    url(r'^finish_pending/', views.finish_pending, name='finish_pending'),
    url(r'^(?P<trip_id>[0-9]+)/pending_paynow/', views.pending_paynow, name='pending_paynow'),
]