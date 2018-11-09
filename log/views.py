from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.template.context_processors import csrf


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm


def signup(request):
    return render(request, 'signup.html', {})


def validate_username(request):
    username = request.GET.get('username', None)
    response_data = {
        'is_taken': User.objects.filter(username__iexact==username).exists()
    }
    if response_data['is_taken']:
        response_data['error_message'] = 'Пользователь с таким именем уже существует.'
    return JsonResponse(response_data)


def login(request):
    kwargs = {}
    kwargs.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            kwargs['login_error'] = 'Пользователь не найден.'
    return render(request, 'log.html', kwargs)


def logout(request):
    '''auth.logout(request)
    return redirect('/')'''
    auth.logout(request)
    response = redirect('/')
    return render(request, response)
