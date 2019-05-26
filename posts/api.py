from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.serializer import PostListSerializer, PostSerializer


class PostsAPI(ListCreateAPIView):

    queryset = Post.objects.all().select_related('author')

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer


class PostAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all().select_related('author')
    serializer_class = PostSerializer
