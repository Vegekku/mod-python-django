from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from posts.models import Post


def latest_posts(request):
    posts = Post.objects.all().order_by('-publish_date')

    context = {'latest_posts': posts}

    html = render(request, 'posts/latest.html', context)

    return HttpResponse(html)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {'post': post}

    html = render(request, 'posts/detail.html', context)

    return HttpResponse(html)
