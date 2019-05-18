from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from posts.forms import PostForm
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


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post created successfully with ID {0}'.format(new_post.pk))
            form = PostForm()
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'posts/new.html', context)
