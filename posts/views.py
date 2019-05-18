from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def latest_posts(request):
    posts = Post.objects.all()

    context = {'latest_posts': posts}

    html = render(request, 'posts/latest.html', context)

    return HttpResponse(html)
