from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def group_list(request, slug):
    return render(request, 'posts/group_list.html')
