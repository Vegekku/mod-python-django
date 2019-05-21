from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from posts.forms import PostForm
from posts.models import Post


class LatestPostsView(View):

    def get(self, request, username=None):
    #def get(self, request):
        # menor a la fecha actual
        # username = None
        # if username is not None:
        # user = User.objects.get(username=username)
        # posts = user.get('posts').objects.all()
        # queryset = queryset.filter(Q(visibility=Photo.PUBLIC) | Q(owner=self.request.user))
        # posts = Post.objects.filter(Q(publish_date__lte=datetime.now) & Q(author=user)).order_by('-publish_date')
        #    posts = Post.objects.all().filter(publish_date__lte=datetime.now).order_by('-publish_date')
        # else:
        #    posts = Post.objects.all().filter(publish_date__lte=datetime.now).order_by('-publish_date')

        posts = Post.objects.all().order_by('-publish_date')

        context = {'latest_posts': posts}

        html = render(request, 'posts/latest.html', context)

        return HttpResponse(html)


class PostDetailView(View):
    def get(self, request, username, pk):
    #def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

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
