from django.conf.urls import url
from . import views
from . import search


app_name = 'property'
urlpatterns = [
    # url(r'^$', views.property_signup, name='welcome'),
    url(r'^$', views.add_property,name="add_property"),
    url(r'^(?P<property_id>[0-9]+)/$', views.property_detail, name='property_detail'),
    url(r'^results/', search.simple_search, name="simple_search"),
    url(r'^multi_results/', search.multi_search, name="multi_search"),
    url(r'^add_review/', views.add_review, name="add_review"),

]