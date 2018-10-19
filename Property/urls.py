from django.conf.urls import url
from . import views
from . import search


app_name = 'property'
urlpatterns = [
    # url(r'^$', views.property_signup, name='welcome'),
    url(r'^add_property/', views.add_property,name="add_property"),

    url(r'^list_property/$', views.list_property, name='list_property'),
    url(r'^(?P<property_id>[0-9]+)/details$', views.look_detail_of_myProperty, name='look_detail_of_myProperty'),
    url(r'^(?P<property_id>[0-9]+)/(?P<trip_id>[0-9]+)/$', views.property_detail, name='property_detail'),

    url(r'^(?P<property_id>[0-9]+)/delete_property/$', views.delete_property, name='delete_property'),
    url(r'^(?P<property_id>[0-9]+)/release_property/$', views.release_property, name='release_property'),
    url(r'^(?P<property_id>[0-9]+)/cancel_release/$', views.cancel_release, name='cancel_release'),

    url(r'^(?P<property_id>[0-9]+)/edit_property/$', views.edit_property, name='edit_property'),

    url(r'^results/', search.simple_search, name="simple_search"),
    url(r'^add_review/', views.add_review, name="add_review"),

]