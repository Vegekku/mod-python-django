from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from posts.forms import PostForm
from posts.models import Post


class LatestPostsView(View):

    def get(self, request, username=None):
        if username is not None:
            author = get_object_or_404(User, username=username)
            posts = author.posts.all()
            # another way without 404 page
            # posts = Post.objects.filter(author__username=username)
        else:
            posts = Post.objects.select_related('author').all()

        context = {'latest_posts': posts.filter(publish_date__lte=datetime.now()).order_by('-publish_date')}

        html = render(request, 'posts/latest.html', context)

        return HttpResponse(html)


class PostDetailView(View):
    def get(self, request, username, pk):
        post = get_object_or_404(Post.objects.select_related('author'), pk=pk, publish_date__lte=datetime.now(), author__username=username)

        context = {'post': post}

        html = render(request, 'posts/detail.html', context)

        return HttpResponse(html)


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/new.html', context)

    def post(self, request):
        post = Post()
        post.author = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post created successfully with ID {0}'.format(new_post.pk))
            form = PostForm()
        context = {'form': form}
        return render(request, 'posts/new.html', context)
