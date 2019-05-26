from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'media', 'intro', 'publish_date']


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'intro', 'media', 'body', 'create_date', 'publish_date', 'modification_date', 'categories', 'author']
        read_only_fields = ['id', 'create_date', 'modification_date']