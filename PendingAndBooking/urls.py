from django.conf.urls import url
from . import views

app_name = 'PendingAndBooking'
urlpatterns = [
    url(r'^$', views.booking, name='booking'),
]