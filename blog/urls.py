from rest_framework import routers, serializers, viewsets

from blog.models import Post, Page, Category


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


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = [
            'title',
            'slug',
            'content',
            'created_at',
            'updated_at',
        ]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
        lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'pages', PageViewSet)
router.register(r'categories', CategoryViewSet)
