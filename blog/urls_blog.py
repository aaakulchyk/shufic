from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.show_all_videos),
    re_path(r'^bio$', views.show_bio),
    re_path(r'^video/(?P<video_id>\d+)/$', views.show_video),
    re_path(r'^like_video/(?P<video_id>\d+)/$', views.like_video),
    re_path(r'^like_video/like_video_ajax/$', views.like_video_ajax),
    re_path(r'^dislike_video/(?P<video_id>\d+)/$', views.dislike_video),
    re_path(r'^dislike_video/dislike_video_ajax/$', views.dislike_video_ajax),
    re_path(r'^commit/(?P<video_id>\d+)/$', views.commit),
]