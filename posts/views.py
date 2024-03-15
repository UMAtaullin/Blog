from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):

    posts = Post.objects.all()

    data = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', data)


def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)

    data = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', data)
