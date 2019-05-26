from django.db.models import Q
from django.utils import timezone
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializer import PostListSerializer, PostSerializer


class PostsAPI(ListCreateAPIView):

    permission_classes = [PostPermission]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'body')
    ordering_fields = ('title', 'publish_date')
    ordering = ('-publish_date',)

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.request.user.is_anonymous:
            return queryset.filter(Q(publish_date__lte=timezone.now()))
        elif self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(Q(publish_date__lte=timezone.now()) | Q(author=self.request.user))

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostAPI(RetrieveUpdateDestroyAPIView):

    permission_classes = [PostPermission]

    queryset = Post.objects.all().select_related('author')
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
