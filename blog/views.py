from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from . import form
from django.template.context_processors import csrf
from django.contrib import auth


def show_all_videos(request):
    content = []
    for video in Video.objects.all():
        one_video = [video]
        one_video.append(Comment.objects.filter(videoparent_id=video.id))
        content.append(one_video)
    return render(request, 'home.html', {"content": content, "username": auth.get_user(request).username})


def show_video(request, video_id):
    kwargs = {}
    kwargs.update(csrf(request))
    kwargs['Video'] = Video.objects.get(id=video_id)
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


def like_video_ajax(request):
    if request.GET:
        idvideo = request.GET['like_video']
        video = Video.objects.get(id=idvideo)
        video.Video_likos += 1
        video.save()
    return HttpResponse(video.rating)


def dislike_video(request, video_id):
    response = redirect('/video/' + str(video_id) + '/')
    if video_id in request.COOKIES:
        Video.objects.get(id=video_id).rating += 1
        response.delete_cookie(video_id)
    else:
        Video.objects.get(id=video_id).rating -= 1
        response.set_cookie(video_id, 'I don\'t like it!')
    return response


def dislike_video_ajax(request):
    if request.GET:
        video = Video.objects.get(id=request.GET['dislike_video'])
        video.rating -= 1
        video.save()
    return HttpResponse(video.rating)


def commit(request, video_id):
    if request.POST:
        _form = form.CommentForm(request.POST)
        if _form.is_valid():
            comment = _form.save(commit=False)
            comment.videoparent = Video.objects.get(id=video_id)
            _form.save()
    return redirect('/video/' + str(video_id) + '/')
