from django.urls import re_path
from . import views


app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.show_latest_videos, name='home'),
    re_path(r'^bio$', views.show_bio, name='bio'),
    re_path(r'^video/(?P<video_id>\d+)/$', views.show_video, name='video'),
    re_path(r'^ajax/like_video/$', views.like_video, name='like_video'),
    re_path(r'^ajax/dislike_video/$', views.dislike_video, name='dislike_video'),
    re_path(r'^ajax/leave_comment/$', views.leave_comment, name='leave_comment'),
]