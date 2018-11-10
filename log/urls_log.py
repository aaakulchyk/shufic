from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'log'
urlpatterns = [
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', views.log_out, name='logout'),
    re_path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    #re_path(r'^ajax/validate_password/$', views.validate_password, name='vaidate_password),
]