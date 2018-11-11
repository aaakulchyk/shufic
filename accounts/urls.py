from django.urls import re_path
from . import views


urlpatterns = [
    re_path('signup/', views.SignUp.as_view(), name='signup'),
]