from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf


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
    auth.logout(request)
    return redirect('/')
