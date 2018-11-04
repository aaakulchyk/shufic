from django.urls import re_path
from . import views


app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.show_latest_videos),
    re_path(r'^bio$', views.show_bio, name='bio'),
    re_path(r'^video/(?P<video_id>\d+)/$', views.show_video, name='video'),
    re_path(r'^video/(?P<video_id>\d+)/like/$', views.toggle_like_video, name='like_video'),
    re_path(r'^/ajax/like_video/$', views.like_video_ajax, name='like_video_ajax'),
    re_path(r'^video/(?P<video_id>\d+)/dislike/$', views.toggle_dislike_video, name='dislike_video'),
    #re_path(r'^/ajax/dislike_video/$', views.dislike_video_ajax, name='dislike_video_ajax  '),
    re_path(r'^video/(?P<video_id>\d+)/leave_comment/$', views.leave_comment, name='leave_comment'),
]