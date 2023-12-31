from rest_framework import serializers, viewsets

from blog.models import Post
from blog.view_sets.category_view_set import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'thumbnail',
            'content',
            'excerpt',
            'category',
            'created_at',
            'updated_at',
            'comment_count',
        ]


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.select_related('category').prefetch_related('comments')
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        highlight = self.request.query_params.get('highlight')

        if category is not None:
            queryset = queryset.filter(category__slug = category)
        elif highlight is not None and highlight == 'true':
            queryset = queryset.filter(highlight = True)
        return queryset
