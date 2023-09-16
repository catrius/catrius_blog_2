from rest_framework import serializers, viewsets

from blog.models import Post
from blog.view_sets.category_view_set import CategorySerializer
from blog.view_sets.comment_view_set import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    comments = CommentSerializer(many = True)

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
            'comments',
        ]


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.select_related('category').prefetch_related('post')
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.select_related('category')
        category = self.request.query_params.get('category')
        highlight = self.request.query_params.get('highlight')

        if category is not None:
            queryset = queryset.filter(category__slug = category)
        elif highlight is not None and highlight == 'true':
            queryset = queryset.filter(highlight = True)
        return queryset
