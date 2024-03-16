from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Post, Group


def index(request):

    post_list = Post.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    data = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', data)


@login_required
def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)

    data = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', data)
