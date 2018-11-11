from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Video, Comment
from django.template.context_processors import csrf
from django.contrib import auth
import json


def show_latest_videos(request):
    most_recent_videos_list = Video.objects.order_by('-date')
    paginator = Paginator(most_recent_videos_list, 12)
    page = request.GET.get('page')
    most_recent_videos = paginator.get_page(page)
    context = {
        'videos': most_recent_videos,
    }
    return render(request, 'home.html', context)


def show_most_recent_videos(request):
    return show_latest_videos(request)


def show_most_rated_videos(request):
    most_rated_videos_list = Video.objects.order_by('-rating')
    paginator = Paginator(most_rated_videos_list, 12)
    page = request.GET.get('page')
    most_rated_videos = paginator.get_page(page)
    context = {
        'videos': most_rated_videos,
    }
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


def like_video(request):
    video_id = request.GET.get('video_id')
    video = Video.objects.get(id=video_id)
    video.rating += 1
    video.save()
    return HttpResponse(video.rating)


def dislike_video(request):
    video_id = request.GET.get('video_id')
    video = Video.objects.get(id=video_id)
    video.rating -= 1
    video.save()
    return HttpResponse(video.rating)


def leave_comment(request):
    if request.POST:
        videoparent = Video.objects.get(id=request.POST.get('video_id'))
        text = request.POST.get('text')
        comment = Comment(videoparent=videoparent, text=text)
        comment.save()
        response_data = {
            'text': comment.text,
            'rating': comment.rating,
        }
        return HttpResponse(json.dumps(response_data), content_type='application/json')


def like_comment(request):
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.get(id=comment_id)
    comment.rating += 1
    comment.save()
    return HttpResponse(comment.rating)


def dislike_comment(request):
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.get(id=comment_id)
    comment.rating -= 1
    comment.save()
    return HttpResponse(comment.rating)


def search(request):
    query = request.GET.get('query')
    queried_videos_list = Video.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    paginator = Paginator(queried_videos_list, 5)
    page = request.GET.get('page')
    queried_videos = paginator.get_page(page)
    context = {
        'videos': queried_videos,
    }
    return render(request, 'search.html', context)
