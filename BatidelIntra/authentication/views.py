from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'authentication/login.html', {
            'error_message': "Mauvaises informations de connection.",
        })


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'authentication/login.html')