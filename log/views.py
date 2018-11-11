from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.template.context_processors import csrf
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def signup(request):
    return render(request, 'signup.html', {})


def validate_username(request):
    username = request.GET.get('username', None)
    response_data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if response_data['is_taken']:
        response_data['error_message'] = 'Пользователь с таким именем уже существует.'
    return JsonResponse(response_data)


def verify_username(request):
    username = request.GET.get('username')
    response_data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if response_data['is_taken']:
        response_data['error_message'] = 'Пользователь с таким именем не найден.'
    return JsonResponse(response_data)


def log_in(request):
    print("WYSISYG" + request.POST)
    context = {}.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    auth_page = request.POST.get('page', 'login.html')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, auth_page, context)
    else:
        context['error_message'] = 'Invalid user.'
        return render(request, auth_page, context)


def log_out(request):
    auth_page = request.POST.get('page')
    logout(request)
    return redirect(auth_page)
