from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, Comment
from . import form
from django.template.context_processors import csrf
from django.contrib import auth


def show_latest_videos(request):
    latest_videos_list = Video.objects.order_by('-date')[:10]
    context = {'latest_videos_list': latest_videos_list,}
    return render(request, 'home.html', context)


def show_video(request, video_id):
    kwargs = {}
    kwargs.update(csrf(request))
    kwargs['Video'] = get_object_or_404(Video, id=video_id)
    kwargs['Comments'] = Comment.objects.filter(videoparent_id=video_id)
    kwargs['Form'] = form.CommentForm
    kwargs['Username'] = auth.get_user(request).username
    return render(request, 'video.html', kwargs)


def show_bio(request):
    return render(request, 'bio.html', {})


def toggle_like_video(request, video_id):
    response = redirect('/video/' + str(video_id) + '/')
    video = Video.objects.get(id=video_id)
    cookies = request.COOKIES
    if video_id in cookies:
        if cookies[video_id] == 'dislike':
            video.rating += 2
            response.set_cookie(video_id, 'like')
        elif cookies[video_id] == 'like':
            video.rating -= 1
            response.delete_cookie(video_id)
    else:
        video.rating += 1
        response.set_cookie(video_id, 'like')
    video.save()
    return response


def toggle_dislike_video(request, video_id):
    response = redirect('/video/' + str(video_id) + '/')
    video = Video.objects.get(id=video_id)
    cookies = request.COOKIES
    if video_id in cookies:
        if cookies[video_id] == 'like':
            video.rating -= 2
            response.set_cookie(video_id, 'dislike')
        elif cookies[video_id] == 'dislike':
            video.rating += 1
            response.delete_cookie(video_id)
    else:
        video.rating -= 1
        response.set_cookie(video_id, 'dislike')
    video.save()
    return response


def commit(request, video_id):
    if request.POST:
        _form = form.CommentForm(request.POST)
        if _form.is_valid():
            comment = _form.save(commit=False)
            comment.videoparent = Video.objects.get(id=video_id)
            _form.save()
    return redirect('/video/' + str(video_id) + '/')
