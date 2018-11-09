from django.urls import re_path
from . import views


app_name = 'log'
urlpatterns = [
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    #re_path(r'^ajax/validate_password/$', views.validate_password, name='vaidate_password),
]