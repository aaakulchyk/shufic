from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Video, Comment
from django.template.context_processors import csrf
from django.contrib import auth

def show_latest_videos(request):
    latest_videos_list = Video.objects.order_by('-date')[:10]
    context = {'latest_videos_list': latest_videos_list,}
    return render(request, 'home.html', context)


def show_video(request, video_id):
    context = {'video': get_object_or_404(Video, id=video_id),
               'comments': Comment.objects.filter(videoparent_id=video_id),
               'username': auth.get_user(request).username,
               'form': CommentForm, }
    context.update(csrf(request))
    return render(request, 'video.html', context)


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


def leave_comment(request, video_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.videoparent = Video.objects.get(id=video_id)
            form.save()
    return redirect("/video/" + str(video_id) + "/")