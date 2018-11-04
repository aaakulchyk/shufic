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


def like_video(request, video_id):
    if video_id not in request.COOKIES:
        video = Video.objects.get(id=video_id)
        video.Video_likos += 1
        video.save()
        response = redirect('/video/' + str(video_id) + '/')
        response.set_cookie(video_id, 'I like it!')
        return response
    return redirect('/video/' + str(video_id) + '/')


def dislike_video(request, video_id):
    response = redirect('/video/' + str(video_id) + '/')
    if video_id in request.COOKIES:
        Video.objects.get(id=video_id).rating += 1
        response.delete_cookie(video_id)
    else:
        Video.objects.get(id=video_id).rating -= 1
        response.set_cookie(video_id, 'I don\'t like it!')
    return response


def commit(request, video_id):
    if request.POST:
        _form = form.CommentForm(request.POST)
        if _form.is_valid():
            comment = _form.save(commit=False)
            comment.videoparent = Video.objects.get(id=video_id)
            _form.save()
    return redirect('/video/' + str(video_id) + '/')
