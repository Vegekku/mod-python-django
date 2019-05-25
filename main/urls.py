"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import LatestPostsView, PostDetailView, CreatePostView
from users.api import UsersAPI, UserAPI
from users.views import LoginView, LogoutView, SignUpView, ListView

api_path = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignUpView.as_view(), name='signup'),
    # Blogs
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('blogs/<str:username>', LatestPostsView.as_view(), name='user_blog'),
    path('blogs', ListView.as_view(), name='list_blogs'),
    # Posts
    path('new-post', CreatePostView.as_view(), name='create_post'),
    path('', LatestPostsView.as_view(), name='home'),

    # API
    path('{0}/users/<int:pk>'.format(api_path), UserAPI.as_view(), name='user_api'),
    path('{0}/users'.format(api_path), UsersAPI.as_view(), name='users_api'),
]
