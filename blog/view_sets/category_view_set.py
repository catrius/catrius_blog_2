from rest_framework import serializers, viewsets

from blog.models import Category
from blog.view_sets.post_view_set import PostSerializer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many = True, read_only = True)

    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'posts',
        ]
        lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('posts')
    serializer_class = CategorySerializer
    lookup_field = 'slug'
