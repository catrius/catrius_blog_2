from rest_framework import serializers, viewsets

from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only = True,
        slug_field = 'name'
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'thumbnail',
            'content',
            'excerpt',
            'category',
            'created_at',
            'updated_at',
        ]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('category')
    serializer_class = PostSerializer
    lookup_field = 'slug'
