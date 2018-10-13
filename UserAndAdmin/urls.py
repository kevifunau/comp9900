from django.conf.urls import url
from django.urls import path


from . import views

app_name = 'userandadmin'
urlpatterns = [
    url(r"^$",views.index,name="index"),
    url(r'^login/', views.login, name = 'login'),
    url(r'^register/', views.register,name="register"),
    url(r'^logout/', views.logout,name="logout"),
    url(r'^editprofile/(?P<page_id>[0-9]+)$', views.editprofile,name="editprofile"),
    url(r'^accountsetting', views.accountsetting,name="accountsetting"),

]