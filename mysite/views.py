from django.shortcuts import render
from django.conf.urls import handler404


def index(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/dashboard.html', {'user': request.user})
    return render(request, 'mysite/index.html')
